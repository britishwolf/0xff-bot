import discord
from discord.ext import commands

import string

class Ciphers():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="caesar",
            description="Caesar's cipher",
            brief="Caesar's cipher")
    async def caesar(self, shift : int, plaintext : str):
        if abs(shift) > 25:
            await self.bot.say("Shift integer is too large!")
            return

        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet, shifted_alphabet)
        await self.bot.say("```%s```" % plaintext.translate(table))

    @commands.command(name="vigenere",
            description="Vigenere cipher",
            brief="Vigenere cipher")
    async def vigenere(self, mode : str, plaintext : str, key: str):

        allowed_modes = ["d", "decrypt", "decode", "e", "encrypt", "encode"]
        if not mode in allowed_modes:
            await self.bot.say("Invalid mode")
            return

        k_len = len(key)
        k_ints = [ord(i) for i in key]
        txt_ints = [ord(i) for i in plaintext]
        ret_txt = ""
        for i in range(len(txt_ints)):
            adder = k_ints[i % k_len]
            if mode[0] == 'd':
                adder *= -1

            v = (txt_ints[i] - 32 + adder) % 95

            ret_txt += chr(v + 32)

        await self.bot.say("```%s```" % ret_txt)
