/* Work in progress */

print('Variance : {}'.format(var))
    fig, ax = plt.subplots(nrows=1, ncols=1, facecolor="#F0F0F0")  #define a figure
    plot_acf(df,ax=ax)                   #autocorrelation plot
    plt.show()                     #show the figure
    autocov = acovf(df)            #autocovariance
    print('Autocovariance : {}'.format(autocov))
    df['pandas_SMA_60'] = df.iloc[:,0].rolling(window=60).mean()   #orizoume moving average
    df['seconds'] = range(len(df))    #create a column with the seconds. We use it for the plots
    plt.plot(df['seconds'],df['event'],label= 'Event')    #plot the time serie with respect to the seconds
    plt.plot(df['seconds'],df['pandas_SMA_4'],label= 'MA 60 seconds')   #plot the 60 seconds moving average
    plt.legend(loc='best')
    plt.title('Moving Averages')
    plt.show()
    return df
