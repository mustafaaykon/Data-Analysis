import pandas as pd
dataset = pd.read_csv('/users/mustafaaliaykon/Downloads/mls-salaries-2017.csv')

# first10 = dataset.head(10) => reading first 10 data.
# print(first10)

# print(len(dataset.index)) => total index


# print(dataset["base_salary"].mean()) => mean of the base_salary

# print(dataset["base_salary"].max()) => maximum salary

# print(dataset["guaranteed_compensation"].max()) => maximum guaranteed compensation
# or , dataset[dataset["guaranteed_compensation"] == dataset["guaranteed_compensation"].max()["last_name"].iloc[0]]
# => iloc[0] bize sadece 'kaka' ismini verdi.


# print(dataset.nlargest(1,["guaranteed_compensation"])["last_name"].iloc[0]) #=> finding largest guaranteeed compensation,lastname and informatinons.

# print(dataset[dataset["last_name"] == "Gonzalez Pirez"]["position"].iloc[0]) => Gonzales Pirez's position.

# print(dataset.groupby("position").mean()) => groupby position and means

# print(dataset["position"].nunique()) => number of different positions.

# print(dataset["position"].value_counts()) => number of players for each position.

# print(dataset["club"].value_counts()) => number of players for each club.

# def son_find(last_name):
#     if "son" in last_name.lower():
#         return True                                   => player who has 'son' in lastname
#     return False

# print(dataset[dataset["last_name"].apply(son_find)])


