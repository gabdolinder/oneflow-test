import mysqlFunc


def main():
    sql_file_path = "oneflowDB.sql"

    table_mappings = {
        "user": "user_analytics",
        "account": "account_analytics",
    }

    connection = mysqlFunc.create_connection()

    if connection:
        # Create the databases if they don't exist
        mysqlFunc.create_databases(connection)

        # Run the SQL file in the database to create and fill production tables
        mysqlFunc.create_prod_tables(sql_file_path)

        # Create the analytics tables if they don't exist
        mysqlFunc.create_analytics_tables(connection)

        # Populate the analytics tables with production data
        for source_table, destination_table in table_mappings.items():
            mysqlFunc.fetch_and_insert_data(connection, source_table, destination_table)

        # Close the connection
        connection.close()


if __name__ == "__main__":
    main()
