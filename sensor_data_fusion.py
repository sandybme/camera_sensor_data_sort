import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import argparse


def fuse_sensor_data(grouped_data,filename,threshold=2.0):
    header_written = False
    for timestamp, group in grouped_data:
        # print(timestamp,group)
        coords = group[['x_position', 'y_position']].values
        #DBSCAN clusteres based on distance by fitting x and y coordinates or positions
        clustered_db = DBSCAN(eps=threshold, min_samples=1, metric='euclidean').fit(coords)
        labels = clustered_db.labels_
        unique_labels = np.unique(labels)
        fuse_data =[]
        #processing the ids for the clusters
        for label in unique_labels:
            cluster_data = group[labels == label]
            datetime_values = pd.to_datetime(cluster_data['timestamp_id']).view(np.int64)
            avg_timestamp = pd.Timestamp(datetime_values.mean()).isoformat(timespec='milliseconds') + "Z"

            # print(avg_timestamp)


            known_unique_ids = cluster_data[cluster_data['unique_id'] != 0]['unique_id'].unique()
            if len(known_unique_ids) > 0:
                f_u_id = known_unique_ids[0]
            else:
                f_u_id = 0
        
            cluster_list = cluster_data[['x_position', 'y_position', 'sensor_id']].values.tolist()

            fuse_data.append({
                'f_timestamp': avg_timestamp,
                'f_id': np.random.randint(1, 1000000), 
                'cluster_data': cluster_list,
                'f_u_id': f_u_id
            })
        fuse_data_df = pd.DataFrame(fuse_data)
        fuse_data_df.to_csv(filename, mode='a', header=(not header_written), index=False)
        header_written = True

def main():

    parser = argparse.ArgumentParser(description="Fuse sensor data")
    parser.add_argument('--input_file', default='test_Data.csv',type=str, required=False, help="input file path")
    parser.add_argument('--output_file',default='fused_Data.csv',type=str, required=False, help="output file path")
    parser.add_argument('--threshold', type=float, default=2.0, help="Distance threshold")
    args = parser.parse_args()

    data = pd.read_csv(args.input_file)
    # inorder to read data by timestamp sequentially, I sort and group data by the 'timestamp_id'
    sorted_data_ts = data.sort_values(by="timestamp_id")
    grouped_data_ts = sorted_data_ts.groupby('timestamp_id')


    threshold_distance = args.threshold
    filename = args.output_file
    fuse_sensor_data(grouped_data_ts,filename,threshold=threshold_distance)

if __name__ == '__main__':
    main()