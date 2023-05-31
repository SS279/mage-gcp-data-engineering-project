if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    # Drop duplicates in dataframe and reset index
    df = df.drop_duplicates().reset_index(drop=True)

    # Rename column names
    df.rename(columns = {'RowNumber':'RowId', 'Geography':'Country', 'EstimatedSalary':'Salary'}, inplace = True)
    customer_churn_data = df
    
    return {"customer_churn_data":customer_churn_data.to_dict(orient="dict")}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'