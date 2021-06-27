def name_file(old_name: str, new_name=''):
    """Name the new worksheet."""

    old_name = old_name if not old_name.endswith('.csv') else old_name[:-4]
    if new_name:
        if new_name.endswith('.csv'):
            return new_name
        else:
            return f'{new_name}.csv'
    else:
        return f'{old_name}_cleaned.csv'
