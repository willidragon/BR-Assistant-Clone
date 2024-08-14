# tools.py

import pandas as pd
from langchain.agents import tool
from pydantic import BaseModel, Field

# Load the CSV file
df = pd.read_csv("backend/src/files/recipe.csv")

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
    field_name: str = Field(..., title="Field Name", description="The name of the field to change.")
    new_value: str = Field(..., title="New Value", description="The new value to set for the specified field.")

# Define the LangChain tool for changing a field's data
@tool(args_schema=ChangeFieldDataInput)
def change_field_data(product_id: str, field_name: str, new_value: str) -> str:
    """
    Change the value of a specified field for a given product ID.
    """
    try:
        # Filter the dataframe based on the product ID
        product_row = df[df['ProductID'] == product_id]
        
        if product_row.empty:
            return f"No record found for Product ID: {product_id}"
        
        # Update the field with the new value
        df.loc[df['ProductID'] == product_id, field_name] = new_value
        
        # Return a success message
        return f"Updated '{field_name}' for Product ID '{product_id}' to: {new_value}"
    
    except KeyError:
        return f"Field '{field_name}' does not exist in the CSV file."


print(convert_to_openai_function(get_recipe_field))
print(convert_to_openai_function(change_field_data))