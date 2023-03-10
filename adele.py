import discord
from discord.ext import commands
import os
import asyncio
TOKEN  = "MTA4MTExODg4OTU1MjkyNDc0Mg.GUdHb2.zI7KVQE_G4xj2-09d9Y5WHx7GLNCJsc4v-hXwA" #トークン
PREFIX = '>'       #prefix=接頭辞
#bgmコマンドで使う再生キュー
class AudioQueue(asyncio.Queue):
    def __init__(self):
        super().__init__(0)         #再生キューの上限を設定しない
    def __getitem__(self, idx):
        return self._queue[idx]     #idx番目を取り出し
    def to_list(self):
        return list(self._queue)    #キューをリスト化
    def reset(self):
        self._queue.clear()         #キューのリセット
#bgmコマンドで使う，現在の再生状況を管理するクラス
class AudioStatus:
    def __init__(self, vc):
        self.vc = vc                                #自分が今入っているvc
        self.queue = AudioQueue()                   #再生キュー
        self.playing = asyncio.Event()
        asyncio.create_task(self.playing_task())
    #曲の追加
    async def add_audio(self, path):
        await self.queue.put(path)
    #曲の再生（再生にはffmpegが必要）    
    async def playing_task(self):
        while True:
            self.playing.clear()
            try:
                path = await asyncio.wait_for(self.queue.get(), timeout = 100)
            except asyncio.TimeoutError:
                asyncio.create_task(self.leave())
            selfpath = os.path.dirname(__file__)
            self.vc.play(discord.FFmpegPCMAudio(path),after = self.play_next)
            await self.playing.wait()
    
    #playing_taskの中で呼び出される
    #再生が終わると次の曲を再生する
    def play_next(self, err=None):
        self.bgminfo = None
        self.playing.set()
        return
            
    #vcから切断
    async def leave(self):
        self.queue.reset()  #キューのリセット
        if self.vc:
            await self.vc.disconnect()
            self.vc = None
        return
    
#botの作成
bot = commands.Bot(command_prefix=PREFIX , intents=discord.Intents.all())
Audio_queue = None #AudioStatusの宣言
#予め決めておいた音楽ファイルを再生する
@bot.command()
async def track00(ctx):
    """play music"""
    global Audio_queue   #この関数内ではVCはグローバル変数のVCを指す
    if (ctx.author.voice is None):  #送信者がボイスチャンネルにいなければエラーを返す
        await send_message(ctx.send, ctx.author.mention, 'ボイスチャンネルが見つかりません')
        return
    if ((Audio_queue is None) or (Audio_queue.vc is None)):      #botがボイスチャンネルに入っていなければ
        voice_channel = ctx.author.voice.channel.id                     #送信者の入っているボイスチャンネルのID
        vc = await bot.get_channel(voice_channel).connect()             #ボイスチャンネルに入る
        Audio_queue = AudioStatus(vc)
    path = 'bgm/music.mp3'    #このファイルが置いてあるディレクトリまでのファイルパス
    #music.mp3をキューに追加
    await Audio_queue.add_audio('bgm/music.mp3')
    return

@bot.command()
async def track01(ctx):
    """play music"""
    global Audio_queue   #この関数内ではVCはグローバル変数のVCを指す
    if (ctx.author.voice is None):  #送信者がボイスチャンネルにいなければエラーを返す
        await send_message(ctx.send, ctx.author.mention, 'ボイスチャンネルが見つかりません')
        return
    if ((Audio_queue is None) or (Audio_queue.vc is None)):      #botがボイスチャンネルに入っていなければ
        voice_channel = ctx.author.voice.channel.id                     #送信者の入っているボイスチャンネルのID
        vc = await bot.get_channel(voice_channel).connect()             #ボイスチャンネルに入る
        Audio_queue = AudioStatus(vc)
    path = 'bgm/ashicoki.mp3'     #このファイルが置いてあるディレクトリまでのファイルパス
    #music.mp3をキューに追加
    await Audio_queue.add_audio('bgm/ashicoki.mp3')
    return

@bot.command()
async def morning(ctx):
    """play music"""
    global Audio_queue   #この関数内ではVCはグローバル変数のVCを指す
    if (ctx.author.voice is None):  #送信者がボイスチャンネルにいなければエラーを返す
        await send_message(ctx.send, ctx.author.mention, 'ボイスチャンネルが見つかりません')
        return
    if ((Audio_queue is None) or (Audio_queue.vc is None)):      #botがボイスチャンネルに入っていなければ
        voice_channel = ctx.author.voice.channel.id                     #送信者の入っているボイスチャンネルのID
        vc = await bot.get_channel(voice_channel).connect()             #ボイスチャンネルに入る
        Audio_queue = AudioStatus(vc)
    path = 'morning.mp3'    #このファイルが置いてあるディレクトリまでのファイルパス
    #music.mp3をキューに追加
    await Audio_queue.add_audio('morning.mp3')
    return

@bot.command()
async def doctor(ctx):
    """play music"""
    global Audio_queue   #この関数内ではVCはグローバル変数のVCを指す
    if (ctx.author.voice is None):  #送信者がボイスチャンネルにいなければエラーを返す
        await send_message(ctx.send, ctx.author.mention, 'ボイスチャンネルが見つかりません')
        return
    if ((Audio_queue is None) or (Audio_queue.vc is None)):      #botがボイスチャンネルに入っていなければ
        voice_channel = ctx.author.voice.channel.id                     #送信者の入っているボイスチャンネルのID
        vc = await bot.get_channel(voice_channel).connect()             #ボイスチャンネルに入る
        Audio_queue = AudioStatus(vc)
    path = 'bgm/doctor.mp3'    #このファイルが置いてあるディレクトリまでのファイルパス
    #music.mp3をキューに追加
    await Audio_queue.add_audio('bgm/doctor.mp3')
    return

@bot.command()
async def magic(ctx):
    """play music"""
    global Audio_queue   #この関数内ではVCはグローバル変数のVCを指す
    if (ctx.author.voice is None):  #送信者がボイスチャンネルにいなければエラーを返す
        await send_message(ctx.send, ctx.author.mention, 'ボイスチャンネルが見つかりません')
        return
    if ((Audio_queue is None) or (Audio_queue.vc is None)):      #botがボイスチャンネルに入っていなければ
        voice_channel = ctx.author.voice.channel.id                     #送信者の入っているボイスチャンネルのID
        vc = await bot.get_channel(voice_channel).connect()             #ボイスチャンネルに入る
        Audio_queue = AudioStatus(vc)
    path = 'bgm/magic.mp3'    #このファイルが置いてあるディレクトリまでのファイルパス
    #music.mp3をキューに追加
    await Audio_queue.add_audio('bgm/magic.mp3')
    return

'''
@bot.command()
async def kongyo(ctx):
    """play music"""
    global Audio_queue   #この関数内ではVCはグローバル変数のVCを指す
    if (ctx.author.voice is None):  #送信者がボイスチャンネルにいなければエラーを返す
        await send_message(ctx.send, ctx.author.mention, 'ボイスチャンネルが見つかりません')
        return
    if ((Audio_queue is None) or (Audio_queue.vc is None)):      #botがボイスチャンネルに入っていなければ
        voice_channel = ctx.author.voice.channel.id                     #送信者の入っているボイスチャンネルのID
        vc = await bot.get_channel(voice_channel).connect()             #ボイスチャンネルに入る
        Audio_queue = AudioStatus(vc)
    path = 'kongyo.mp3'    #このファイルが置いてあるディレクトリまでのファイルパス
    #music.mp3をキューに追加
    await Audio_queue.add_audio('kongyo.mp3')
    return
'''

@bot.command()
async def lookme(ctx):
    """play music"""
    global Audio_queue   #この関数内ではVCはグローバル変数のVCを指す
    if (ctx.author.voice is None):  #送信者がボイスチャンネルにいなければエラーを返す
        await send_message(ctx.send, ctx.author.mention, 'ボイスチャンネルが見つかりません')
        return
    if ((Audio_queue is None) or (Audio_queue.vc is None)):      #botがボイスチャンネルに入っていなければ
        voice_channel = ctx.author.voice.channel.id                     #送信者の入っているボイスチャンネルのID
        vc = await bot.get_channel(voice_channel).connect()             #ボイスチャンネルに入る
        Audio_queue = AudioStatus(vc)
    path = 'lookme.mp3'    #このファイルが置いてあるディレクトリまでのファイルパス
    #music.mp3をキューに追加
    await Audio_queue.add_audio('lookme.mp3')
    return


@bot.command()
async def yankumi(ctx):
    """play music"""
    global Audio_queue   #この関数内ではVCはグローバル変数のVCを指す
    if (ctx.author.voice is None):  #送信者がボイスチャンネルにいなければエラーを返す
        await send_message(ctx.send, ctx.author.mention, 'ボイスチャンネルが見つかりません')
        return
    if ((Audio_queue is None) or (Audio_queue.vc is None)):      #botがボイスチャンネルに入っていなければ
        voice_channel = ctx.author.voice.channel.id                     #送信者の入っているボイスチャンネルのID
        vc = await bot.get_channel(voice_channel).connect()             #ボイスチャンネルに入る
        Audio_queue = AudioStatus(vc)
    path = 'yankumi.mp3'    #このファイルが置いてあるディレクトリまでのファイルパス
    #music.mp3をキューに追加
    await Audio_queue.add_audio('yankumi.mp3')
    return

@bot.command()
async def tanaka(ctx):
    """play music"""
    global Audio_queue   #この関数内ではVCはグローバル変数のVCを指す
    if (ctx.author.voice is None):  #送信者がボイスチャンネルにいなければエラーを返す
        await send_message(ctx.send, ctx.author.mention, 'ボイスチャンネルが見つかりません')
        return
    if ((Audio_queue is None) or (Audio_queue.vc is None)):      #botがボイスチャンネルに入っていなければ
        voice_channel = ctx.author.voice.channel.id                     #送信者の入っているボイスチャンネルのID
        vc = await bot.get_channel(voice_channel).connect()             #ボイスチャンネルに入る
        Audio_queue = AudioStatus(vc)
    path = 'tanaka.mp3'    #このファイルが置いてあるディレクトリまでのファイルパス
    #music.mp3をキューに追加
    await Audio_queue.add_audio('tanaka.mp3')
    return


@bot.command()
async def door(ctx):
    """play music"""
    global Audio_queue   #この関数内ではVCはグローバル変数のVCを指す
    if (ctx.author.voice is None):  #送信者がボイスチャンネルにいなければエラーを返す
        await send_message(ctx.send, ctx.author.mention, 'ボイスチャンネルが見つかりません')
        return
    if ((Audio_queue is None) or (Audio_queue.vc is None)):      #botがボイスチャンネルに入っていなければ
        voice_channel = ctx.author.voice.channel.id                     #送信者の入っているボイスチャンネルのID
        vc = await bot.get_channel(voice_channel).connect()             #ボイスチャンネルに入る
        Audio_queue = AudioStatus(vc)
    path = 'door.mp3'    #このファイルが置いてあるディレクトリまでのファイルパス
    #music.mp3をキューに追加
    await Audio_queue.add_audio('door.mp3')
    return

@bot.command()
async def hmm(ctx):
    """play music"""
    global Audio_queue   #この関数内ではVCはグローバル変数のVCを指す
    if (ctx.author.voice is None):  #送信者がボイスチャンネルにいなければエラーを返す
        await send_message(ctx.send, ctx.author.mention, 'ボイスチャンネルが見つかりません')
        return
    if ((Audio_queue is None) or (Audio_queue.vc is None)):      #botがボイスチャンネルに入っていなければ
        voice_channel = ctx.author.voice.channel.id                     #送信者の入っているボイスチャンネルのID
        vc = await bot.get_channel(voice_channel).connect()             #ボイスチャンネルに入る
        Audio_queue = AudioStatus(vc)
    path = 'hmm.mp3'    #このファイルが置いてあるディレクトリまでのファイルパス
    #music.mp3をキューに追加
    await Audio_queue.add_audio('hmm.mp3')
    return


'''
@bot.command()
async def drx(ctx):
    """play music"""
    global Audio_queue   #この関数内ではVCはグローバル変数のVCを指す
    if (ctx.author.voice is None):  #送信者がボイスチャンネルにいなければエラーを返す
        await send_message(ctx.send, ctx.author.mention, 'ボイスチャンネルが見つかりません')
        return
    if ((Audio_queue is None) or (Audio_queue.vc is None)):      #botがボイスチャンネルに入っていなければ
        voice_channel = ctx.author.voice.channel.id                     #送信者の入っているボイスチャンネルのID
        vc = await bot.get_channel(voice_channel).connect()             #ボイスチャンネルに入る
        Audio_queue = AudioStatus(vc)
    path = 'drx.mp3'    #このファイルが置いてあるディレクトリまでのファイルパス
    #music.mp3をキューに追加
    await Audio_queue.add_audio('drx.mp3')
    return
'''


'''@bot.command()
async def crazydr(ctx):
    """play music"""
    global Audio_queue   #この関数内ではVCはグローバル変数のVCを指す
    if (ctx.author.voice is None):  #送信者がボイスチャンネルにいなければエラーを返す
        await send_message(ctx.send, ctx.author.mention, 'ボイスチャンネルが見つかりません')
        return
    if ((Audio_queue is None) or (Audio_queue.vc is None)):      #botがボイスチャンネルに入っていなければ
        voice_channel = ctx.author.voice.channel.id                     #送信者の入っているボイスチャンネルのID
        vc = await bot.get_channel(voice_channel).connect()             #ボイスチャンネルに入る
        Audio_queue = AudioStatus(vc)
    path = 'crazy.mp3'    #このファイルが置いてあるディレクトリまでのファイルパス
    #music.mp3をキューに追加
    await Audio_queue.add_audio('crazy.mp3')
    return
'''


#botをボイスチャンネルから切断する
'''@bot.command()
async def remove(ctx):
    await Audio_queue.leave()
    return
'''
#例のアレ
@bot.command()
async def about(ctx):
    await ctx.send('''～あらすじ～
    敵軍に捕まってしまった主人公(あなた)、目を覚ますと敵の将校であるアデーレが目の前にいた。
    アデーレに気に入られてしまった主人公は、アデーレにエッチな調教をされることに……
    最初は抵抗する主人公だったが、すぐにアデーレのいいなりになり……


    ■01足コキ(匂い攻め　乳首攻め　ツバローション)　[15:12]

    　ストッキングの匂いを嗅がされ足コキされる。

    「いいぞそのまま続けろ……もっと嗅いで私の匂いで頭の中いっぱいにしろ……ご主人様の匂いをしっかり覚えるんだ……」
    「なぁ、この我慢汁でヌルヌつになったち○ぽに私のツバを足したらどうなるだろうなぁ……」
    「いいぞ……頭からっぽにしていっぱい出すんだ……ほら、命令だ、足の匂い嗅ぎがら情けなく敗北おもらしするんだ……」


    ■02オナサポ (軽いオナ指示　匂い攻め) [16:58]

    　股の匂いを嗅がされながらオナニーさせられる。

    「キスが好きなんだな……クスクス。だったら、上手にシコシコってオナニーできたらあとでもっーとキスしてやる……」
    「ご主人様の匂いを嗅ぐとすぐ発情してしまう情けないち○ぽ……もっと扱くんだ……いいぞ、もっともっと私の匂いを覚えて気持ちよくなるんだ……クスクス」
    「オナニーも射精もぜーんぶ私に支配されて情けなくおねだりして射精させてもらう……それでいいんだ、全部私に委ねてしまえ……そうすれば気持ちよくしてやるからな……」


    ■03下着コキ (キス　乳首攻め　好き)　[16:24]

    　パンツをち○ぽに被せて手コキされる。

    「さっきまで私のアソコ、おま○こが触れていた部分を……亀頭に被せて……ほーら、できた。やらしいな……クスクス」
    「クスクス、乳首弄られながら下着に犯されて喜んでるだけでも恥ずかしいのに、喘ぎ声まで漏らして……お前は本当にどうしようもない変態だな……」
    「いいんだぞ、気持ちよくなって……どんなに情けない姿でも私はお前の事が大好きだぞ……クスクス。お前も私の事好きだろう?」



    ■04逆正常位　(キス　耳舐め　好き　謝罪) [16:23]

    　好きって言われたりごめんなさいって言わされながら逆正常位で犯される。

    「もっと犯されたい、もっとめちゃくちゃにして欲しい……大好きなアデーレ様に犯してもらえて幸せ……そうだろう?クスクス……」
    「耳犯されながら好きって言われる度に頭が痺れて脳が犯されてるみたいだな……好き好きって声が漏れてしまっていたぞ……」
    「犯されながらしっかりゴメンナサイするんだぞ……心から謝るんだ……ご主人様大好きです。もう逆らいません、いい子になりますーって……クスクス。」



    ■05_おまけ(足コキの初期案)(足舐め　乳首攻め　ツバローション) [14:55]

    　足を舐めさせられながら足コキされる。(基本的に足コキシーンと同じです)

    「見下されて、足をしゃぶりながらマゾち○ぽ踏まれるの気持ちいい……いくら否定しようがお前はどうしようもなく変態でマゾなんだ……」
    「本当はわかってるんだろ?　負けちゃダメだって……でも、もう気持ち良くなる事で頭がいっぱい……もう何も考えられない……もっともっと気持ちよくなりたい……敗北おもらししたい……」



    再生時間合計　1時間24分24秒


    CV.沢野ぽぷら様''')
    return
bot.run(TOKEN)
