# Data Dictionary


## nav_history.csv

| Column Name | Data Type | Business Definition                     | Source          |
| ----------- | --------- | --------------------------------------- | --------------- |
| amfi_code   | INTEGER   | Unique identifier of mutual fund scheme | nav_history.csv |
| date        | DATE      | NAV reporting date                      | nav_history.csv |
| nav         | FLOAT     | Net Asset Value per unit                | nav_history.csv |

## scheme_performance.csv

| Column Name | Data Type | Business Definition                     | Source                 |
| ----------- | --------- | --------------------------------------- | ---------------------- |
| amfi_code   | INTEGER   | Mutual fund scheme identifier           | scheme_performance.csv |
| return_1y   | FLOAT     | One year return percentage              | scheme_performance.csv |
| return_3y   | FLOAT     | Three year annualized return percentage | scheme_performance.csv |
