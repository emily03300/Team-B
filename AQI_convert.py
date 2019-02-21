############################ AQI table ##################################
#AQI              0-50,  51-100, 101-150, 151-200, 201-300, 301-400, 401-500
#index               0,       1,       2,       3,       4,       5,       6,
#MAX (038, O31, PM25, CO, SO2, NO2, AQI)
O3_8Max_AqiArray  = [54, 70, 85, 105, 200,  0,  0]
O3_1MaxAqiArray   = [ 0, 0, 164, 204, 404, 504, 604]
PM25_MaxAqiArray  = [12.0, 35.4, 55.4, 150.4, 250.4, 350.4, 500.4]
CO_MaxAqiArray    = [4.4, 9.4, 12.4, 15.4, 30.4, 40.4, 50.4]
SO2_MaxAqiArray   = [35, 75, 185, 304, 604, 804, 1004]
NO2_MaxAqiArray   = [53, 100, 360, 649, 1249, 1649, 2049]
Aqi_MaxAqiArray   = [50, 100, 150, 200, 300, 400, 500]

#MIN (038, O31, PM25, CO, SO2, NO2, AQI)
O3_8Min_AqiArray  = [0, 55, 71, 86, 106, 0, 0]
O3_1MinAqiArray   = [ 0, 0, 125, 165, 205, 405, 505]
PM25_MinAqiArray  = [0.0, 12.1, 35.5, 55.5, 150.5, 250.5, 350.5]
CO_MinAqiArray    = [0.0, 4.5, 9.5, 12.5, 15.5, 30.5, 40.5]
SO2_MinAqiArray   = [0, 36, 76, 186, 305, 605, 805]
NO2_MinAqiArray   = [0, 54, 101, 361, 650, 1250, 1650]
Aqi_MinAqiArray   = [0, 51, 101, 151, 201, 301, 401]
#######################################################################


def AQI_convert( c , air):
    c_low = 0.0
    c_high = 0.0
    i_low = 0.0
    i_high = 0.0
    I = 0.0

    if (air == 'PM25'):
        for i in range(0, 7):
            if ( PM25_MinAqiArray[i] <= c <= PM25_MaxAqiArray[i] ):
                c_low = PM25_MinAqiArray[i];
                c_high = PM25_MaxAqiArray[i];
                i_low = Aqi_MaxAqiArray[i];
                i_high = Aqi_MinAqiArray[i];
                break;

    elif (air == 'CO'):
        for i in range(0, 7):
            if ( CO_MinAqiArray[i] <= c <= CO_MaxAqiArray[i] ):
                c_low = CO_MinAqiArray[i];
                c_high = CO_MaxAqiArray[i];
                i_low = Aqi_MaxAqiArray[i];
                i_high = Aqi_MinAqiArray[i];
                break;
            else:
                print("data out of range")
    elif (air == 'SO2'):
        for i in range(0, 7):
            if ( SO2_MinAqiArray[i] <= c <= SO2_MaxAqiArray[i] ):
                c_low = SO2_MinAqiArray[i];
                c_high = SO2_MaxAqiArray[i];
                i_low = Aqi_MaxAqiArray[i];
                i_high = Aqi_MinAqiArray[i];
                break;
            else:
                print("data out of range")
    elif (air == 'NO2'):
        for i in range(0, 7):
            if ( NO2_MinAqiArray[i] <= c <= NO2_MaxAqiArray[i] ):
                c_low = NO2_MinAqiArray[i];
                c_high = NO2_MaxAqiArray[i];
                i_low = Aqi_MaxAqiArray[i];
                i_high = Aqi_MinAqiArray[i];
                break;
            else:
                print("data out of range")

    ###################computing AQI formula####################
    I = (((i_high - i_low)/(c_high - c_low))*(c-c_low)) + i_low
    ############################################################

    if (air == 'O3'):
        c_low = 0.0
        c_high = 0.0
        i_low = 0.0
        i_high = 0.0
        I = 0.0
        I_O3_8=0.0
        I_03_1=0.0
        for i in range(0, 7):
            if (O3_8Min_AqiArray[i] <= c <= O3_8Max_AqiArray[i]):
                c_low = PM25_MinAqiArray[i];
                c_high = PM25_MaxAqiArray[i];
                i_low = Aqi_MaxAqiArray[i];
                i_high = Aqi_MinAqiArray[i];
                I_O3_8 = (((i_high - i_low) / (c_high - c_low)) * (c - c_low)) + i_low
                break;
            else:
                print("data out of range")
        for i in range(0, 7):
            if (O3_1MinAqiArray <= c <= O3_1MaxAqiArray[i]):
                c_low = PM25_MinAqiArray[i];
                c_high = PM25_MaxAqiArray[i];
                i_low = Aqi_MaxAqiArray[i];
                i_high = Aqi_MinAqiArray[i];
                I_O3_1 = (((i_high - i_low) / (c_high - c_low)) * (c - c_low)) + i_low
                break;
            else:
                print("data out of range")

    return I;


print(AQI_convert( 1200 , 'NO2'))