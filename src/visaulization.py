import matplotlib.pyplot as plt
import pandas as pd

def plot_lat_long(df: pd.DataFrame, landmarks: float, points: str):
    """Función para graficar los mapas de new york de los puntos de subida y de ajada

    Args:
        df (pd.DataFrame): DataFrame
        landmarks (float): Important places
        points (str): Use 'Pickup', 'Dropoff'
    """
    plt.style.use('ggplot')
    if points.lower() == 'pickup':
        fig, ax = plt.subplots(1,1,figsize=(10,10))
        ax.plot(list(df.pickup_longitude),
                list(df.pickup_latitude),
                '.',markersize=1)
    else:
        fig, ax = plt.subplots(1,1,figsize=(10,10))
        ax.plot(list(df.dropoff_longitude),
                list(df.dropoff_latitude),
                '.',markersize=1)
        
    for landmark in landmarks:
        ax.plot(landmarks[landmark][0],
                landmarks[landmark][1],
                '*', markersize=15,
                alpha = 1,
                color = 'red')
        plt.annotate(landmark,(landmarks[landmark][0]+0.005,
                    landmarks[landmark][1]+.005),
                     color='red',
                     backgroundcolor='white')
    plt.grid(None)  
    ax.set_xlabel('Latitude')
    ax.set_ylabel('Longitude')
    ax.set_title(f'{points} Locations in NYC Illustrated')
    plt.show()   