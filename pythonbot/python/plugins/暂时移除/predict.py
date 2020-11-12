# -*- coding: utf-8 -*-
import numpy as np
import tensorflow.compat.v1 as tf
from nonebot import on_command, CommandSession
from .contents import HEROES_LIST_PREDICT
tf.reset_default_graph() 
tf.disable_eager_execution()

def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result

xs = tf.placeholder(tf.float32, [None, 260])
ys = tf.placeholder(tf.float32, [None, 2])

l1 = add_layer(xs, 260, 100, activation_function=tf.nn.softmax)
l2 = add_layer(l1, 100, 40, activation_function=tf.nn.softmax)
prediction = add_layer(l2, 40, 2, activation_function=tf.nn.softmax)
          
            
saver = tf.train.Saver()#saver
sess = tf.Session()

@on_command('predict', aliases=('预测'),only_to_me=False)
async def predict(session: CommandSession):
    heroes = session.get('heroes', prompt='你想查询哪个阵容呢？')
    heroes=heroes.split('-')
    prediction = await predict_radiant_win(heroes)

    await session.send(prediction)



@predict.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['heroes'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询的阵容不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg


async def predict_radiant_win(heroes: str) -> str:
    synergy =np.load("synergy.npy", allow_pickle=True)
    counter =np.load("counter.npy", allow_pickle=True)
    saver.restore(sess, "my_net/save_net.ckpt") 
    strresult=''
    hero_id=np.zeros([1,260])
    radiant_hero=np.zeros([1,5])
    dire_hero=np.zeros([1,5])
    for i in range(10):
        index=np.where(HEROES_LIST_PREDICT==heroes[i])[0][0]
        if i<5:
            hero_id[0][index]=1
            radiant_hero[0][i]=index
        else:
            hero_id[0][index+130]=1
            dire_hero[0][i-5]=index
    for j in range(5):
            for k in range(5):
                if j!=k:
                    hero_id[0][0]+=synergy[int(radiant_hero[0][j])][int(radiant_hero[0][k])]
                    hero_id[0][130]+=synergy[int(dire_hero[0][j])][int(dire_hero[0][k])]           
            hero_id[0][117]+=counter[int(radiant_hero[0][j])][int(dire_hero[0][k])]
    y_pre = sess.run(prediction, feed_dict={xs: hero_id})       
            
    strresult='天辉胜率：'+str(y_pre[0][1])+'夜魇胜率'+str(y_pre[0][0])       
    return str(strresult)
            
            
            
            
            
            
            