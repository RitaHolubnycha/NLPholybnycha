
import pandas as pd

def load_split(data_path):
    df = pd.read_csv(data_path)

    train = df[df["split"]=="train"]
    val   = df[df["split"]=="dev"]
    test  = df[df["split"]=="test"]

    return train, val, test


if __name__ == "__main__":

    train,val,test = load_split("data/processed_v2/processed_v2.csv")

    print("Train:",len(train))
    print("Validation:",len(val))
    print("Test:",len(test))
