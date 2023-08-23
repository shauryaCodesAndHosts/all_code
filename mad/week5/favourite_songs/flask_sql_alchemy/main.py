import os
from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
current_dir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(current_dir, 'songsdb.sqlite3')

db= SQLAlchemy()
db.init_app(app)
app.app_context().push()

# setup is done , now everthing else remains the same we just use db witheveything

class Singer(db.Model):
    __tablename__ = 'singers'
    singer_id=db.Column(db.Integer,autoincrement=True,primary_key=True,unique=True,nullable=False)
    name=db.Column(db.String,nullable=False)
    insta_handle=db.Column(db.String,nullable=True)
    songs=db.relationship('Song',secondary='song_singers')

class Song(db.Model):
    __tablename__= 'songs'
    song_id=db.Column(db.Integer,autoincrement=True,primary_key=True,unique=True)
    name= db.Column(db.String,nullable=False)
    Lyrics= db.Column(db.String,nullable=False)
    Url=db.Column(db.String,nullable=False)
    #singers=relationship('Singer',secondary='song_singers')

class SongSinger(db.Model):
    __tablename__ = 'song_singers'
    song_id=db.Column(db.Integer,db.ForeignKey('songs.song_id'), nullable= False, primary_key=True)
    singer_id=db.Column(db.Integer,db.ForeignKey('singers.singer_id'), primary_key=True,nullable=False)


@app.route('/',methods=['GET','POST'])
def home():
    singers=Singer.query.all()
    print(type(singers))
    singer_name_song={}
    for s in singers:
        print(s.name)
        singer_name_song[s.name]=[]
        for su in s.songs:
            print(su.name)
            singer_name_song[s.name].append(su)
            print(type(singer_name_song[s.name][0]))
    print("***********")
    print(singer_name_song)
    return render_template('songs.html', singers=singer_name_song)
    '''    #with Session(engine) as session:
    #    singers= session.query(Singer).all()
    #    for singer in singers:
    #        print(singer.name)
    #        print("**********")
    #        for song in singer.songs:
    #            print(song.name)
    #        print("**********")
    #        print("**********")
    '''


@app.route('/singer/<singer_name>',methods=['GET','POST'])
def songs_play(singer_name):
    all_singers=Singer.query.all()
    for ss in all_singers:
        if ss.name == singer_name:
            print(ss.songs)
            break
    print("****************")
    print()
    return render_template('singer_songs_play.html',singer=ss)







if __name__ == "__main__":
    app.run(host='0.0.0.0' ,port =8080, debug=True )
