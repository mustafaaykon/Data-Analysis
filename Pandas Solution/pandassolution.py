import pandas as pd
import argparse


class Solution:
    def __init__(self):
        ## Display ##
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        self.files = self.read_files()

    def read_files(self):
        ## Read all csv files
        product = pd.read_csv("product.csv")
        sales = pd.read_csv("sales.csv")
        store = pd.read_csv("store.csv")

        return {"product": product,
                "sales": sales,
                "store": store}

    def run(self, start_date, end_date, top_n=3):
        product_with_sales_df = pd.merge(self.files["product"],
                                         self.files["sales"],
                                         how="outer",
                                         left_on="id",
                                         right_on="product")

        clean_df = pd.merge(product_with_sales_df,
                            self.files["store"],
                            how="outer",
                            left_on="store",
                            right_on="id")

        ## date filter ##
        df = clean_df[(clean_df['date'] > start_date) &
                      (clean_df['date'] <= end_date)].sort_values(
            by=['quantity'],
            ascending=False).reset_index(drop=True)

        case_list = ["city", "store", "brand", "product"]
        for item in case_list:
            ## top N ##
            top_seller_df = df.groupby(item).describe()["quantity"]["count"]
            top_seller_df = pd.DataFrame(top_seller_df).reset_index().sort_values("count", ascending=False).reset_index(
                drop=True)
            print('''-- Top seller {} --'''.format(item))
            print(top_seller_df.head(top_n))
            print('-------------------------------------')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    This script is calculate sales etc.""")
    parser.add_argument("--MinDate", help="Minimum date")
    parser.add_argument("--MaxDate", help="Maximum date")
    parser.add_argument("--Top", help="Top N value")

    args = parser.parse_args()

    Solution().run(start_date=args.MinDate,
                   end_date=args.MaxDate,
                   top_n=int(args.Top))
