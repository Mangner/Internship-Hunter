import sqlalchemy as sa

engine = sa.create_engine("sqlite:///:memory:")
connection = engine.connect()

metadata = sa.MetaData()

offers_table = sa.Table(
    "offers",
    metadata,
    sa.Column("offer_id", sa.Integer, primary_key=True, autoincrement=True),
    sa.Column("offer_name", sa.String),
    sa.Column("creation_date", sa.String),
    sa.Column("expiration_date", sa.String),
    sa.Column("link", sa.String)
)

def insert_offer(offer_name: str, creation_date: str, expiration_date: str, link: str):
    query = offers_table.insert().values(
        offer_name=offer_name, 
        creation_date=creation_date, 
        expiration_date=expiration_date,
        link=link
    )
    connection.execute(query)



def main():
    metadata.create_all(engine)
    insert_offer("Staż", "10.10.2025", "10.03.2026", "https://www.youtube.com/watch?v=aAy-B6KPld8")
    connection.close()

main()