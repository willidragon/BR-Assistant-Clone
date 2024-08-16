# tools.py

import pandas as pd
from langchain.agents import tool
from pydantic import BaseModel, Field
import logging

# Load the CSV file
df = pd.read_csv("src/files/recipe.csv")

# Define the list of available fields
available_fields_description = (
    "GroupType, GroupID, GroupExclude, Fab, Tech, Func, ProductID, MAIN_PD, OPE_NO, "
    "STAGE_ID, MODULEPD_ID, PD_ID, OPE_NAME, LR_SRC, LCRECIPE_ID, EQP, RECIPE_GROUP, "
    "ER_DESC, RTCLGRP_ID, RETICLEUDATA, QT_OPERNO, QT_DURATION_OOC, QT_DURATION_OOS, "
    "QT_ACTION_TYPE, QT_WAT_NOTE, REWORK_JOIN, REWORK_REWORK, REWORK_CNT, SUBROUTE_OP_NO, "
    "SUBROUTE_MAIN, DCDEF_PREV_OPE_NO, DCDEF_DELTA_DCDEF_ID, DCDEF_ID1, DCDEF_ID2, DCDEF_ID3, "
    "DCDEF_ID4, DCDEF_ID5, DCDEF_ID6, DCDEF_ID7, DCDEF_ID8, DCDEF_ID9, DCDEF_ID10, DCSPEC_SRC, "
    "DCSPEC_ID, DCSPEC_DESC, DDCSPEC_ID, DDCSPEC_DESC, PRE1_SCRIPT_IDENT, POST_SCRIPT_IDENT, "
    "SPC_CORR, RESP_NO, PG_ID, RECIPE_ID1, RECIPE_ID2, RECIPE_ID3, RECIPE_ID4, RECIPE_ID5, "
    "RECIPE_ID6, RECIPE_ID7, RECIPE_ID8, RECIPE_ID9, RECIPE_ID10, PROCESS_CNT, CUR_SETUP_STATE, "
    "CUST, PRE_DCDEF, SMP_FLAG"
)

@tool
def list_all_product_ids() -> str:
    """
    Return a list of all Product IDs in the CSV file.
    """
    
    logging.info("list_all_product_ids called")
    
    try:
        # Get all unique Product IDs
        product_ids = df['ProductID'].unique().tolist()
        logging.info(f"Found {len(product_ids)} Product IDs")
        
        # Return the list as a string
        return "\n".join(product_ids)
    
    except Exception as e:
        logging.error(f"An unexpected error occurred while listing Product IDs: {str(e)}")
        return "An unexpected error occurred while listing Product IDs."

# Define the input schema
class GetRecipeFieldInput(BaseModel):
    product_id: str = Field(..., title="Product ID", description="The ID of the product to search for.")
    field_name: str = Field(..., title="Field Name", description="The name of the field to retrieve.")


# Define the LangChain tool
@tool (args_schema=GetRecipeFieldInput)
def get_recipe_field(product_id: str, field_name: str) -> str:
    """
    Search the CSV file for a given product ID and return the specified field.
    """

    logging.info(f"get_recipe_field called with ProductID: {product_id} and FieldName: {field_name}")
    
    try:
        # Filter the dataframe based on the product ID
        product_row = df[df['ProductID'] == product_id]
        
        if product_row.empty:
            return f"No record found for Product ID: {product_id}"
        
        # Return the requested field
        value = product_row[field_name].values[0]
        return f"The value of '{field_name}' for Product ID '{product_id}' is: {value}"
    
    except KeyError:
        return f"Field '{field_name}' does not exist in the CSV file."
    
# Define the input schema for changing a field's data
class ChangeFieldDataInput(BaseModel):
    product_id: str = Field(..., title="Product ID", description="The ID of the product to change.")
    field_name: str = Field(..., title="Field Name", description=f"The name of the field to change. Available fields are: {available_fields_description}")
    new_value: str = Field(..., title="New Value", description="The new value to set for the specified field.")

# Define the LangChain tool for changing a field's data
@tool(args_schema=ChangeFieldDataInput)
def change_field_data(product_id: str, field_name: str, new_value: str) -> str:
    """
    Change the value of a specified field for a given product ID.
    """

    logging.info(f"Attempting to change field '{field_name}' for Product ID '{product_id}' to '{new_value}'")

    try:
        # Filter the dataframe based on the product ID
        product_row = df[df['ProductID'] == product_id]
        
        if product_row.empty:
            logging.warning(f"No record found for Product ID: {product_id}")
            return f"No record found for Product ID: {product_id}"
        
        # Update the field with the new value
        df.loc[df['ProductID'] == product_id, field_name] = new_value
        logging.info(f"Successfully updated '{field_name}' for Product ID '{product_id}' to '{new_value}'")

        # Save the updated DataFrame back to the CSV file
        df.to_csv("src/files/recipe.csv", index=False)
        logging.info("Changes saved to CSV file.")
        
        # Return a success message
        return f"Updated '{field_name}' for Product ID '{product_id}' to: {new_value}"
    
    except KeyError:
        logging.error(f"Field '{field_name}' does not exist in the CSV file.")
        return f"Field '{field_name}' does not exist in the CSV file."
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return "An unexpected error occurred."

