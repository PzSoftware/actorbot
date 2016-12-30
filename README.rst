========
APIBot
========

A simple python implementation `Odyn <www.odynapp.com>_ bot API
======================================================

Features
========
Python puro com asyncio e aiohttp
* Conexão websocket para ws API wss API-endpoint
* Enviar e receber mensagens
* Módulo API


Módulo API
==========

- Mensagens: SendMessage, UpdateMessageContent

- Grupos: CreateGroup, CreateGroupWithOwner, UpdateShortName, AddGroupExtString, AddGroupExtBool, RemoveExt, InviteUser

- KeyValue: SetVAlue, GetValue, DeleteValue, GetKeys

- Arquivos: UploadFile, DownloadFile

- Etiquetas: CreateStickerPack, AddSticker, ShowStickerPacks, ShowStickers, DeleteSticker, MakeStickerPackDefault, UnmakeStickerPackDefault,

- Bots: CriarBot

- Usuários: FindUser, ChangeUserName, ChangeUserNickname, ChangeUserAbout, ChangeUserAvatar, IsAdmin, AddSlashCommand, RemoveSlashCommand, AddUserExtString, AddUserExtBool, RemoveUserExt

- WebHooks: RegisterHook, GetHooks

Requisitos
============

* Python> = 3.5.1
* `Aiohttp> = 0.22.0 <https://github.com/KeepSafe/aiohttp>` _
* Async_timeout> = 1.1.0 (opcional)


Começando
================


Faça a sua própria conversa herdada da classe base * Conversação *. Por exemplo, simple echo bot (mais em `Wiki <https://github.com/PzSoftware/actorbot/wiki>` _):

.. code-block :: python

    De actorbot.bots import Conversação
    De mensagens de importação de actorbot.api


    Classe EchoConversation (Conversação):
        "" Simples echo bot "" "
        Async def message_handler (self, mensagem):
            Out_msg = messaging.SendMessage (self._get_id (),
                                            Peer = self._peer,
                                            Message = mensagem)
            Aguardar self.send (out_msg)

        Async def response_handler (self, mensagem):
            Aguarde super (). Response_handler (mensagem)


Executar um ou mais bots através do iniciador:

.. code-block :: python

    from actorbot import Bot
    from actorbot.bots import EchoConversation

    ...

    Ownbot = Bot (endpoint = 'YOUR_ACTOR_SERVER_ENDPOINT',
                 Token = 'YOUR_BOT_TOKEN',
                 Name = 'SOME_BOT_NAME',
                 Conversa = EchoConversation)

    Bots = [ownbot]

    Transports = [asyncio.ensure_future (bot.transport.run ()) para bot em bots]
    Processors = [asyncio.ensure_future (bot.run ()) para bot em bots]

    Loop.run_until_complete (asyncio.wait (transportes + processadores))

    ...





