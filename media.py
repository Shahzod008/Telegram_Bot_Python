from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.types import FSInputFile

album_albebra = MediaGroupBuilder()
for i_1 in range(15, 19):
    album_albebra.add_photo(FSInputFile("file/{i_1}.png"))

album_geomerish = MediaGroupBuilder()
for i_2 in range(19, 26):
    album_geomerish.add_photo(FSInputFile("file/{i_2}.png"))

album_fisish = MediaGroupBuilder()
for i_3 in range(26, 34):
    album_fisish.add_photo(FSInputFile("file/{i_3}.png"))

album_rusish = MediaGroupBuilder()
for i_4 in range(41, 50):
    album_rusish.add_photo(FSInputFile("file/{i_4}.png"))