import sqlalchemy 
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Singer(Base):
    __tablename__ = 'singers'
    singer_id=Column(Integer,autoincrement=True,primary_key=True,unique=True,nullable=False)
    name=Column(String,nullable=False)
    insta_handle=Column(String,nullable=True)
    songs=relationship('Song',secondary='song_singers')

class Song(Base):
    __tablename__= 'songs'
    song_id=Column(Integer,autoincrement=True,primary_key=True,unique=True)
    name= Column(String,nullable=False)
    Lyrics= Column(String,nullable=False)
    Url=Column(String,nullable=False)
    #singers=relationship('Singer',secondary='song_singers')

class SongSinger(Base):
    __tablename__ = 'song_singers'
    song_id=Column(Integer,ForeignKey('songs.song_id'), nullable= False, primary_key=True)
    singer_id=Column(Integer, ForeignKey('singers.singer_id'), primary_key=True,nullable=False)

engine=create_engine("sqlite:///./songsdb.sqlite3")

if __name__== '__main__':
    
    #without using the session 

    #stmt=select(Singer)
    #print(stmt)
    #with engine.connect() as conn:
    #    for row in conn.execute(stmt):
    #        print(row)

    # with using the session --> prints singer and then his songs 

    #with Session(engine) as session:
    #    singers= session.query(Singer).all()
    #    for singer in singers:
    #        print(singer.name)
    #        print("**********")
    #        for song in singer.songs:
    #            print(song.name)
    #        print("**********")
    #        print("**********")

    # using transactions 

    #with Session(engine, autoflush=False) as session:
    #    session.begin()
    #    try:
    #        song=Song(
    #            name=input("enter name"),
    #            Lyrics=input("enter the lyrics"),
    #            Url=input("Enter the link ")
    #        )
    #        session.add(song)
    #        session.flush()
    #        song_singer = SongSinger(singer_id=int(input("enter singer id number")), song_id=song.song_id )
    #        session.add(song_singer)
    #    except:
    #        print('rollback')
    #        session.rollback()
    #        raise
    #    else:
    #        print('commit')
    #        session.commit()


    # another way of implemeting

    #with Session(engine, autoflush=False) as session:
    #    session.begin()
    #    try:
    #        singer=session.query(Singer).filter(Singer.name == "RadioHead").one()
    #        song=Song(
    #            name=input("enter name"),
    #            Lyrics=input("enter the lyrics"),
    #            Url=input("Enter the link ")
    #        )
    #        singer.songs.append(song)
    #        session.add(song)
    #
    #    except:
    #        print('rollback')
    #        session.rollback()
    #        raise
    #    else:
    #        print('commit')
    #        session.commit()
    pass