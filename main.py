import pandas as pd

# change leafsnap-dataset-images.txt file into a csv file to make it easier to work with
with open("leafsnap-dataset-images.txt", "r") as data:
    txt = data.read()
    edited_text = txt.replace("	", ",")
    with open("dataset.csv", "w") as new_data:
        new_data.write(edited_text)

# get list of all plant species in dataset
leaf_data = pd.read_csv("dataset.csv")
leaf_list = list(set(leaf_data.species.tolist()))
print(leaf_list)

# create csv file with each leaf and its corresponding common name
leaf_data.species.drop_duplicates().to_csv("leaf_species.csv")

# check leaves.csv file for duplicates or errors
common_names = pd.read_csv("leaves.csv")
print(common_names[["species", "common_name"]])
common_names["common_name"].duplicated().to_csv("check_for_duplicates.csv")

# use leaves.csv to add a common name column to dataset.csv
common_name_list = []
for index, row in leaf_data.iterrows():
    species = row["species"]
    common_name = common_names[common_names["species"] == species].common_name.to_list()[0]
    common_name_list.append(common_name)
leaf_data.insert(4, "common_name", common_name_list, True)
leaf_data.set_index("file_id", inplace=True)
leaf_data.to_csv("dataset.csv")

