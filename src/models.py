import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class friends(Base):
    __tablename__ = 'friends'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    username = Column(String(10), nullable=False) 

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    username = Column(String(10), nullable=False) 
    password = Column(String(250), nullable=False)
    friends_id = Column(Integer, ForeignKey('friends.id'))
    friends = relationship("friends")

class reels(Base):
    __tablename__ = 'reels'
    quality = Column(Integer, primary_key=True)   
    like = Column(Integer, primary_key=True)   
    author = Column(String(250), nullable=False)
    population = Column(Integer, primary_key=True)
    likes_id = Column(Integer, ForeignKey('likes.id'))
    likes = relationship("likes")

class likes(Base):
    __tablename__ = 'likes'
    userid = Column(Integer, primary_key=True)   
    username_id = Column(Integer)   
    amount = Column(Integer)   
    population = Column(Integer) 
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")
    friends_id = Column(Integer, ForeignKey('friends.id'))
    friends = relationship("friends")

class Comment(Base):
    __tablename__ = 'comment'
    userid = Column(Integer, primary_key=True)   
    text = Column(String(250), nullable=False)
    reels_id = Column(Integer, ForeignKey('reels.id'))
    reels = relationship("reels")
    likes_id = Column(Integer, ForeignKey('likes.id'))
    likes = relationship("likes")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")
    friends_id = Column(Integer, ForeignKey('friends.id'))
    friends = relationship("friends")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")
    reels_id = Column(Integer, ForeignKey('reels.id'))
    reels = relationship("reels")
    likes_id = Column(Integer, ForeignKey('likes.id'))
    likes = relationship("likes")
    character_id = Column(Integer, ForeignKey('comment.id'))
    character = relationship("Character")
    

render_er(Base, 'diagram.png')
