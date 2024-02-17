from browser_data import ParserAviator


if __name__ == "__main__":
    start = ParserAviator()
    global_massive = start.corr_text_df()
    while True:
        next_mass = start.corr_text_series()
        result = start.last_edit_text(global_massive, next_mass)