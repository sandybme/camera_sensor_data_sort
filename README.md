# Task_Sentics

Certainly! Here's a README.md for the provided script:

Sensor Data Fusion Script
This script processes a given CSV file containing sensor data, clusters the data based on positions and timestamps, and saves the fused data to a new CSV file.

Requirements
Python 3.x
pandas
scikit-learn
You can install the required packages using:

bash
Copy code
pip install pandas scikit-learn
Usage
To run the script, use the following command:

bash
Copy code
python sensor_data_fusion.py --input_file INPUT_FILE_PATH --output_file OUTPUT_FILE_PATH [--threshold DISTANCE_THRESHOLD]
Arguments:
--input_file INPUT_FILE_PATH: Path to the input CSV file you want to process.

--output_file OUTPUT_FILE_PATH: Path where you want the fused data to be saved.

--threshold DISTANCE_THRESHOLD: (Optional) The distance threshold for clustering. Defaults to 2.0 meters if not provided.

Input CSV Format
The input CSV should have the following columns:

timestamp_id: Timestamp of the sensor reading.
id: ID specific to an individual sensor.
x_position: X-coordinate of the detected object.
y_position: Y-coordinate of the detected object.
unique_id: Universal ID of the detected object. (0 if not known)
sensor_id: ID of the sensor.
Output CSV Format
The output CSV will have the following columns:

f_timestamp: Timestamp of the clustered/fused data.
f_id: Randomly assigned ID for the clustered data.
cluster_data: List of lists containing the x_position, y_position, and sensor_id of the clustered entries.
f_u_id: The unique ID associated with the clustered entries (if available).
