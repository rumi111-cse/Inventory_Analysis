import pandas as pd
import sqlite3
import logging
import time
from ingestion_db import ingest_db

logging.basicConfig(
    filename = "logs/get_vendor_summery.log",
    level = logging.DEBUG,
    format ="%(asctime)s - %(levelname)s - %(message)s",
    filemode = "a"
)

def create_vendor_summery(conn):
    '''this function will merge the different tables to get the overall vendor summary and adding new columns in the resultant data'''
    vendor_sales_summery = pd.read_sql_query("""with frieghtsummery as (
        select
            VendorNumber,
            sum(Freight) as FreightCost
            from vendor_invoice
            group by VendorNumber),
    PurchaseSummery AS (
        Select
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Volume,
            pp.Price as actual_price,
            sum(Quantity) as total_purchase_quantity,
            sum(Dollars) as total_purchase_dollars
            from purchases p
            join purchase_prices pp 
            on p.Brand=pp.Brand
            where p.PurchasePrice>0
            group by p.VendorNumber,p.VendorName,p.Brand, p.Description,p.PurchasePrice,pp.Price,pp.Volume
            ),
    SalesSummery AS (
        select
            VendorNo,
            Brand,
            SUM(SalesDollars) as TotalSalesDollars,
            SUM(SalesPrice) as TotalSalesPrice,
            SUM(SalesQuantity) as TotalSalesQuantity,
            SUM(ExciseTax) as TotalExciseTax
            FROM sales
            group by VendorNo, Brand)

    select
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.Volume,
        ps.actual_price,
        ps.total_purchase_quantity,
        ps.total_purchase_dollars,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalSalesQuantity,
        ss.TotalExciseTax,
        fs.FreightCost
    from PurchaseSummery ps
    left join SalesSummery ss
        on ps.VendorNumber = ss.VendorNo
        and ps.Brand = ss.Brand
    left join frieghtsummery fs
        on ps.VendorNumber = fs.VendorNumber
    order by ps.total_purchase_dollars desc""",conn)

    retrun vendor_sales_summery

def clean_data(df):
    """this function will clean the data"""
    #changing datatypes to float
    df['Volume'] = df.['Volume'].astype('float')

    ##filling missing values with 0
    df.fillna(0,inplace= True)

    #removing spaces from categorical colums
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    ## creating new columns for better analysis

    vendor_sales_summery['GrossProfit'] = vendor_sales_summery['TotalSalesDollars'] -vendor_sales_summery['total_purchase_dollars']
    vendor_sales_summery['ProfitMargin'] =(vendor_sales_summery['GrossProfit'] / vendor_sales_summery['TotalSalesDollars'])*100
    vendor_sales_summery['StockTurnover'] = vendor_sales_summery['TotalSalesQuantity'] / vendor_sales_summery['total_purchase_quantity']
    vendor_sales_summery['SalesPurchaseRatio'] = vendor_sales_summery['TotalSalesDollars']/vendor_sales_summery['total_purchase_dollars']
    return df


if __name__ = '__main__':
    #creating database connections
    conn= sqlite3.connect('inventory.db')

    logging.info('creating vendor summary table...')
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info('cleaning data...')
    clean_df = clean_data(summary_df)
    logging.info(summary_df.head())

    logging.info('Ingesting data...')
    ingest_db(clean_df,'vendor_sales_summery',conn)
    logging.info('completed')