# Data Engineer Workshop - Intro to Data Coding 2024 (DataTH)
**Data Engineer Workshop** เป็น Workshop สุดท้ายของคอร์ส Intro to Data Coding 2024 ในส่วนของ Python ซึ่งจะโฟกัสการทำ ETL (Extrac, Transform, Load) เบื้องต้น ของ Data engineer จะลองสถาณการณ์การทำงานโดยได้รับ Requirement จาก Business Analyst

![image](https://github.com/suben-mk/Python-Workshop-DataTH/assets/89971741/0fd398bf-5778-4ab1-b4cb-b179229191ac)
_Requirement จาก Business Analyst_

## Documents - Specification
### Sales
**source** : dataset-day5.trans_table_full\
**destination** : superstore.sales\
**aggregation** : group by data_date
source_column	| transform	| destination_column | data_type |
------------- | --------- | ------------------ | --------- |
order_date | วันที่สุดท้ายของเดือน |	data_date |	datetime |
sales |	ค่ามากที่สุด |	max_sales |	float |
sales |	ผลรวม |	sum_sales |	float |
quantity |	ค่าเฉลี่ย | 	mean_quantity |	float |
quantity |	ผลรวม |	sum_quantity |	float |
discount |	ผลรวม |	sum_discount |	float |
ship_days |	ค่ามากที่สุด |	max_ship_days |	float |
ship_days |	ค่าน้อยที่สุด |	min_ship_days |	float |

### Sales by Region
**source** : dataset-day5.trans_table_full\
**destination** : superstore.sales_by_region\
**aggregation** : group by data_date, region
source_column	| transform	| destination_column | data_type |
------------- | --------- | ------------------ | --------- |
order_date | วันที่สุดท้ายของเดือน |	data_date |	datetime |
region | ภาค | region |	text |
sales |	ค่ามากที่สุด |	max_sales |	float |
sales |	ผลรวม |	sum_sales |	float |
quantity |	ค่าเฉลี่ย | 	mean_quantity |	float |
quantity |	ผลรวม |	sum_quantity |	float |
discount |	ผลรวม |	sum_discount |	float |
ship_days |	ค่ามากที่สุด |	max_ship_days |	float |
ship_days |	ค่าน้อยที่สุด |	min_ship_days |	float |

### Sales by Category
**source** : dataset-day5.trans_table_full\
**destination** : superstore.sales_by_category\
**aggregation** : group by data_date, category
source_column	| transform	| destination_column | data_type |
------------- | --------- | ------------------ | --------- |
order_date | วันที่สุดท้ายของเดือน |	data_date |	datetime |
category | ประเภทสินค้า |	category | text |
sales |	ค่ามากที่สุด |	max_sales |	float |
sales |	ผลรวม |	sum_sales |	float |
quantity |	ค่าเฉลี่ย | 	mean_quantity |	float |
quantity |	ผลรวม |	sum_quantity |	float |
discount |	ผลรวม |	sum_discount |	float |
ship_days |	ค่ามากที่สุด |	max_ship_days |	float |
ship_days |	ค่าน้อยที่สุด |	min_ship_days |	float |

## Workflow
_**Python libraries :**_ _Pandas, SQLAlchemy_\
Python script และ process ทั้งหมด [Data Engineer Workshop - Intro to Data Coding 2024.py](https://github.com/suben-mk/Python-Workshop-DataTH/blob/main/Data%20Engineer%20Workshop%20-%20Intro%20to%20Data%20Coding%202024.py)

## Output
ผลลัพธ์ Dataset มาตาม Requirement
* Database [superstore.db](https://github.com/suben-mk/Python-Workshop-DataTH/blob/main/Output/superstore.db)
* CSV
  * Order Transection [order_txn.csv](https://github.com/suben-mk/Python-Workshop-DataTH/blob/main/Output/order_txn.csv)
  * Sales [sales.csv](https://github.com/suben-mk/Python-Workshop-DataTH/blob/main/Output/sales.csv)
  * Sales by Region [sales_by_region.csv](https://github.com/suben-mk/Python-Workshop-DataTH/blob/main/Output/sales_by_region.csv)
  * Sales by Category [sales_by_category.csv](https://github.com/suben-mk/Python-Workshop-DataTH/blob/main/Output/sales_by_category.csv)

