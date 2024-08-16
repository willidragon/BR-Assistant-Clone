import psycopg2
import random

# Connection details
conn = psycopg2.connect(
    dbname="mpcs_db",
    user="mpcs_user",
    password="mpcs_password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# List of fruits for generating random data
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Icedragon", "Jackfruit"]

# Function to generate random data
def generate_random_record(fruit_name, index):
    return f"""
    INSERT INTO recipes (
        GroupType, GroupID, GroupExclude, Fab, Tech, Func, ProductID, MAIN_PD, OPE_NO, 
        STAGE_ID, MODULEPD_ID, PD_ID, OPE_NAME, LR_SRC, LCRECIPE_ID, EQP, RECIPE_GROUP, 
        ER_DESC, RTCLGRP_ID, RETICLEUDATA, QT_OPERNO, QT_DURATION_OOC, QT_DURATION_OOS, 
        QT_ACTION_TYPE, QT_WAT_NOTE, REWORK_JOIN, REWORK_REWORK, REWORK_CNT, 
        SUBROUTE_OP_NO, SUBROUTE_MAIN, DCDEF_PREV_OPE_NO, DCDEF_DELTA_DCDEF_ID, 
        DCDEF_ID1, DCDEF_ID2, DCDEF_ID3, DCDEF_ID4, DCDEF_ID5, DCDEF_ID6, DCDEF_ID7, 
        DCDEF_ID8, DCDEF_ID9, DCDEF_ID10, DCSPEC_SRC, DCSPEC_ID, DCSPEC_DESC, 
        DDCSPEC_ID, DDCSPEC_DESC, PRE1_SCRIPT_IDENT, POST_SCRIPT_IDENT, SPC_CORR, 
        RESP_NO, PG_ID, RECIPE_ID1, RECIPE_ID2, RECIPE_ID3, RECIPE_ID4, RECIPE_ID5, 
        RECIPE_ID6, RECIPE_ID7, RECIPE_ID8, RECIPE_ID9, RECIPE_ID10, PROCESS_CNT, 
        CUR_SETUP_STATE, CUST, PRE_DCDEF, SMP_FLAG
    ) VALUES (
        'Fruit_Group', 'GRP-{index}', '{random.choice(['Yes', 'No'])}', 'FAB{random.randint(1,3)}', 
        'Tech{random.choice(['A', 'B', 'C'])}', 'FUNC{random.randint(1,3)}', 
        '300@{index}_{fruit_name.upper()}{index:04d}EM-{random.choice(['A', 'B', 'C'])}', 
        '300@{index}_{fruit_name.upper()}{index:04d}EM-{random.choice(['A', 'B', 'C'])}', 
        '{random.uniform(1000, 9999):.2f}', 'STAGE{random.randint(1, 4)}', 
        '300@{index}_{fruit_name.upper()}{index:04d}EM-{random.choice(['A', 'B', 'C'])}.MOD', 
        '300@{index}_{fruit_name.upper()}{index:04d}EM-{random.choice(['A', 'B', 'C'])}.PD', 
        'Processing {fruit_name}', '300@{index}_{fruit_name.upper()}{index:04d}EM.LR', 
        '300@{index}_{fruit_name.upper()}{index:04d}EM.LCRECIPE', 'EQP-{random.randint(1, 20)}', 
        '{fruit_name}_Group', '{fruit_name} Recipe', 
        '300@{index}_{fruit_name.upper()}{index:04d}EM.RTCL', 'SampleData', 
        'QT-{random.randint(100, 999)}', '{random.randint(1, 10)} mins', 
        '{random.randint(1, 10)} mins', 'Standard', 'Note', 
        'None', 'None', '{random.randint(0, 4)}', 
        'SUB-{random.randint(100, 999)}', 'Main', 
        'D-{random.randint(1, 100)}', 'Delta-{random.randint(1, 100)}', 
        'DCDEF-{random.randint(1, 10)}', 'DCDEF-{random.randint(1, 10)}', 
        'DCDEF-{random.randint(1, 10)}', 'DCDEF-{random.randint(1, 10)}', 
        'DCDEF-{random.randint(1, 10)}', 'DCDEF-{random.randint(1, 10)}', 
        'DCDEF-{random.randint(1, 10)}', 'DCDEF-{random.randint(1, 10)}', 
        'DCDEF-{random.randint(1, 10)}', 'DCDEF-{random.randint(1, 10)}', 
        'SRC-TEST', 'SPEC-ID-{fruit_name.upper()}', 
        '{fruit_name} Description', 'D-SPEC-ID-{fruit_name.upper()}', 
        'D-{fruit_name} Description', '{fruit_name}_PRE1', 
        '{fruit_name}_POST', 'None', 
        'R-{random.randint(1000, 9999)}', 'PG-{random.randint(1000, 9999)}', 
        '{fruit_name}_RECIPE1', '{fruit_name}_RECIPE2', 
        '{fruit_name}_RECIPE3', '{fruit_name}_RECIPE4', 
        '{fruit_name}_RECIPE5', '{fruit_name}_RECIPE6', 
        '{fruit_name}_RECIPE7', '{fruit_name}_RECIPE8', 
        '{fruit_name}_RECIPE9', '{fruit_name}_RECIPE10', 
        '{random.randint(1, 10)}', 'Released', 'Customer', 
        'None', '{random.choice(['Y', 'N'])}'
    );
    """

# Insert multiple records into the database
for index, fruit in enumerate(fruits, start=1):
    sql_command = generate_random_record(fruit, index)
    try:
        print(f"Executing SQL for {fruit}:")
        cursor.execute(sql_command)
        conn.commit()
        print(f"{fruit} data inserted successfully!\n")
    except Exception as e:
        print(f"Error inserting data for {fruit}: {e}\n")

# Close the connection
cursor.close()
conn.close()
