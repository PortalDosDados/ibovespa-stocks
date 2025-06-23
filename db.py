import psycopg2

def connection():
    """Estabelece uma conexão com o banco de dados PostgreSQL e retorna o objeto de conexão."""
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="12345"
        )
        print("Conexão estabelecida com sucesso.")
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None 
        

def close_connection(conn):
    """Fecha a conexão com o banco de dados."""
    if conn:
        try:
            conn.close()
            print("Conexão fechada com sucesso.")
        except psycopg2.Error as e:
            print(f"Erro ao fechar a conexão: {e}")
    else:
        print("Nenhuma conexão para fechar.")


