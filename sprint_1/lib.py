from IPython.display import display, Image
import requests
import re

# While using this library, when creating a dco you have to be accurate with the naming of the object.
# For example, if you want to try the 3D->2D query, you have to declare: variable_name = dco("AvgTemperatureColorScaled")
# If u don't write "AvgTemperatureColorScaled" exactly it won't work. Same for "mean_summer_airtemp" and "AvgLandTemp" respectively.
# You can see examples of how to use each function in the Examples.ipynb file.

class dco(object):
    def __init__(self, datacube):
        self._datacube = datacube

    #Veryfing date format
    def validate_date_format(self, date):
        # Regular expression to match the YYYY-MM format
        pattern = re.compile(r'^\d{4}-\d{2}$')
        if not re.match(pattern, date):
            raise ValueError("Date format must be 'YYYY-MM'.")
        
    #Veryfing latitude range
    def validate_latitude(self, latitude):
        if not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be in the range [-90, 90].")

    #Veryfing longitude range
    def validate_longitude(self, longitude):
        if not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be in the range [-180, 180].")
        
    #mean_summer_airtemp
    def construct_mean_query(self):
        wcps_query = f"""
            for $c in ({self._datacube})
            return encode($c, "png")
            """
        return wcps_query
    
    def mean_query(self):
        final_query = self.construct_mean_query()
        endpoint = 'https://ows.rasdaman.org/rasdaman/ows#/services'
        response = requests.post(endpoint, data = {'query': final_query}, verify=True)
        data = response.content
        return data
    
    #3D->2D AvgTemperatureColorScaled 
    def construct_temp_color_query(self, date):
        #Validating date
        self.validate_date_format(date)
        wcps_query = f"""
            for $c in ({self._datacube})
            return encode(
                $c[ansi("{date}")],
                "image/png"
            )
        """
        return wcps_query
    
    def temp_color_query(self, date):
        final_query = self.construct_temp_color_query(date)
        endpoint = 'https://ows.rasdaman.org/rasdaman/ows#/services'
        response = requests.post(endpoint, data={'query': final_query}, verify=True)
        data = response.content
        return data
    
    #3D->1D AvgLandTemp
    def construct_diagram_query(self, latitude, longitude, start_date, end_date):
        #Validating coordinates
        self.validate_latitude(latitude)
        self.validate_longitude(longitude)
        #Validating dates
        self.validate_date_format(start_date)
        self.validate_date_format(end_date)
        #Making sure start date is before end date
        if start_date >= end_date:
            raise ValueError("Start date must be before the end date.")
        wcps_query = f"""
            for $c in ({self._datacube})
            return encode(
                $c[Lat({latitude}), Long({longitude}), ansi("{start_date}":"{end_date}")],
                "text/csv"
            )
        """
        return wcps_query
    
    def diagram_query(self, latitude, longitude, start_date, end_date):
        final_query = self.construct_diagram_query(latitude, longitude, start_date, end_date)
        endpoint = 'https://ows.rasdaman.org/rasdaman/ows#/services'
        response = requests.post(endpoint, data={'query': final_query}, verify=True)
        data = response.content
        return data
    
    #AvgLandTemp average
    def construct_avg_query(self, latitude, longitude, start_date, end_date):
        #Validating coordinates
        self.validate_latitude(latitude)
        self.validate_longitude(longitude)
        #Validating dates
        self.validate_date_format(start_date)
        self.validate_date_format(end_date)
        #Making sure start date is before end date
        if start_date >= end_date:
            raise ValueError("Start date must be before the end date.")
        wcps_query = f"""
            for $c in ({self._datacube})
            return avg(
                $c[Lat({latitude}), Long({longitude}), ansi("{start_date}":"{end_date}")]
            )
        """
        return wcps_query
    
    def avg_query(self, latitude, longitude, start_date, end_date):
        final_query = self.construct_avg_query(latitude, longitude, start_date, end_date)
        endpoint = 'https://ows.rasdaman.org/rasdaman/ows#/services'
        response = requests.post(endpoint, data={'query': final_query}, verify=True)
        data = response.content
        return data
    
    #AvgLandTemp maximum
    def construct_max_query(self, latitude, longitude, start_date, end_date):
        #Validating coordinates
        self.validate_latitude(latitude)
        self.validate_longitude(longitude)
        #Validating dates
        self.validate_date_format(start_date)
        self.validate_date_format(end_date)
        #Making sure start date is before end date
        if start_date >= end_date:
            raise ValueError("Start date must be before the end date.")
        wcps_query = f"""
            for $c in ({self._datacube})
            return max(
                $c[Lat({latitude}), Long({longitude}), ansi("{start_date}":"{end_date}")]
            )
        """
        return wcps_query
    
    def max_query(self, latitude, longitude, start_date, end_date):
        final_query = self.construct_max_query(latitude, longitude, start_date, end_date)
        endpoint = 'https://ows.rasdaman.org/rasdaman/ows#/services'
        response = requests.post(endpoint, data={'query': final_query}, verify=True)
        data = response.content
        return data
    
    #AvgLandTemp minimum
    def construct_min_query(self, latitude, longitude, start_date, end_date):
        #Validating coordinates
        self.validate_latitude(latitude)
        self.validate_longitude(longitude)
        #Validating dates
        self.validate_date_format(start_date)
        self.validate_date_format(end_date)
        #Making sure start date is before end date
        if start_date >= end_date:
            raise ValueError("Start date must be before the end date.")
        wcps_query = f"""
            for $c in ({self._datacube})
            return min(
                $c[Lat({latitude}), Long({longitude}), ansi("{start_date}":"{end_date}")]
            )
        """
        return wcps_query
    
    def min_query(self, latitude, longitude, start_date, end_date):
        final_query = self.construct_min_query(latitude, longitude, start_date, end_date)
        endpoint = 'https://ows.rasdaman.org/rasdaman/ows#/services'
        response = requests.post(endpoint, data={'query': final_query}, verify=True)
        data = response.content
        return data

