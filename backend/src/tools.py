import pandas as pd
from langchain.agents import tool

# Load the CSV file
df = pd.read_csv("backend/src/files/recipe.csv")

# Define the LangChain tool
@tool
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

# Example usage:
if __name__ == "__main__":
    result = get_recipe_field.invoke({"product_id": "300@3_CPEUVCDU05MVIA000EM-F", "field_name": "RECIPE_ID1"})
    print(result)
