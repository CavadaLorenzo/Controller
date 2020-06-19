import psycopg2


# default value is used when KeyError exception is raised
try:    POSTGRES_IP =  os.environ['POSTGRES_IP'] 
except:    POSTGRES_IP = '192.168.1.190'
try:    POSTGRES_PORT = os.environ['POSTGRES_PORT'] 
except:    POSTGRES_PORT = '54320'
try:    POSTGRES_USER = os.environ['POSTGRES_USER'] 
except:    POSTGRES_USER = 'admin'
try:    POSTGRES_DB_NAME = os.environ['POSTGRES_DB_NAME'] 
except:    POSTGRES_DB_NAME = 'servers'
try:    POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD'] 
except:    POSTGRES_PASSWORD = 'admin'

class PostgresDB:
    def __init__(self):
        """
        Create an object PostgreDB which connect to the given database. 

        :param host: is the database IP
        :param database: is the name of the database
        :param user: is the user used to connect to the database
        :param password: is the password used to connect to the database
        :param port: is the port used to connecto to the database
        """
        self.conn = psycopg2.connect(host = POSTGRES_IP, 
                                    database = POSTGRES_DB_NAME, 
                                    user = POSTGRES_USER, 
                                    password = POSTGRES_PASSWORD,
                                    port = POSTGRES_PORT) 

    def get_all(self):
        """
        This method will return an array of dictionary with all the file in the system.
        Each dictionary will have this structure:
        {
            "id": "sdjkbkjsa",
            "server_id": "server3",
            "filename": "Song2.mp3",
            "copy_date": "2020-06-18 15:19:49"
        }
        """
        select_all_query = f"SELECT * FROM \"File_list\""
        cursor = self.conn.cursor()
        cursor.execute(select_all_query)
        self.conn.commit() 
        return parse_to_array(cursor.fetchall())


def parse_to_array(files):
    file_list = []
    for file in files:
        new_file = {
            "id": file[0],
            "server_id": file[1],
            "filename": file[2],
            "copy_date": file[3]
        }
        file_list.append(new_file)

    return file_list