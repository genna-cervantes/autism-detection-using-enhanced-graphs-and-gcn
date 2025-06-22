import os
import pandas as pd

def convert_1d_to_csv(input_dir, output_dir=None):
    if output_dir is None:
        output_dir = input_dir #overwrite if not set

    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(input_dir):
        if file.endswith(".1D"):
            input_path = os.path.join(input_dir, file)
            output_path = os.path.join(output_dir, file.replace(".1D", ".csv"))

            try:
                df = pd.read_csv(input_path, delim_whitespace=True, header=None)
                df.to_csv(output_path, index=False)
                print(f"Converted {file} → {os.path.basename(output_path)}")
            except Exception as e:
                print(f"Failed to convert {file}: {e}")

convert_1d_to_csv("./abide_timeseries/cc200", "./abide_timeseries/cc200_csv")
convert_1d_to_csv("./abide_timeseries/aal", "./abide_timeseries/aal_csv")
