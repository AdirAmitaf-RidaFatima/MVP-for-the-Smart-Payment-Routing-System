from databases import Database

DATABASE_URL = "postgres://avnadmin:AVNS_8u0YBzy1pLuZRXt-f1_@pg-2da0b7f7-payment-database.h.aivencloud.com:10342/defaultdb?sslmode=require"  # Update with your PostgreSQL credentials

database = Database(DATABASE_URL)
