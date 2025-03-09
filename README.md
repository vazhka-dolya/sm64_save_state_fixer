# SM64 Save State Fixer
When using modern, more accurate graphics plugins on a Nintendo 64 emulator, you may stumble upon a problem where older Super Mario 64 ROM hacks tend to have an issue of pitch black textures in their custom levels. This utility is intended to be used on Super Mario 64 savestates (which are often used for custom levels in machinimas), and it *may* fix that problem in them.
# <img src="https://github.com/vazhka-dolya/sm64_save_state_fixer/blob/main/GitHubResources/showcase_1_1.png"/>
## Why does this problem happen?
In short: in the past there were no accurate graphics plugins and everyone used inaccurate plugins such as Jabo's Direct3D. Older ROM-hacking tools, which were also tested using these inaccurate plugins, assigned surfaces only one certain command for all their color combiners. However, this one command is only intended to work with solid RGBA textures in levels that have fog and will lead to the textures being displayed incorrectly if used in other circumstances (for a more detailed explanation, see [this](https://hack64.net/wiki/doku.php?id=super_mario_64:console_compatibility#improper_use_of_fast3d_s_setcombine_0xfc_command) section in Hack64). But the inaccurate plugins kind of did not really care that the color combiner command was incorrect and displayed the textures normally anyway. This problem was only caught much later when plugins started getting more accurate. This problem with black textures also happens on real Nintendo 64.
## The fix
### In ROM hacks
To fix it in a ROM hack, you can simply open it in a program like [HxD](https://mh-nexus.de/en/hxd/) and replace the wrong color combiner command with the correct one. For older hacks, there are four commands we need to know:
```
FC 12 7E 24 FF FF F9 FC = Solid RGBA texture (No fog)
FC 12 18 24 FF 33 FF FF = Alpha RGBA texture (No fog)
FC 12 7F FF FF FF F8 38 = Solid RGBA texture (With fog)
FC FF FF FF FF FC F2 38 = Alpha RGBA texture (With fog)
```
As stated previously, the older ROM-hacking tools only used the command for a solid RGBA texture with fog for *all* of its textures, which means that we can try replacing `FC 12 7F FF FF FF F8 38` with a correct command from the list. The correct command is often one for the alpha RGBA texture without fog (`FC 12 18 24 FF 33 FF FF`) and it's very possible that you can just do the extreme option of replacing every instance of the command.
### In save states
In save states, it's a little trickier, but nothing too difficult. Z64 ROM hacks are big endian and save states are little endian ([what is an endian?](https://en.wikipedia.org/wiki/Endianness)), which means that we also need to convert the save state from little endian to big endian, only then do the replacement described above, and then convert the changed save state back to little endian. Save states' data is 32-bit integers, which is four bytes.\
\
This utility automates this process for save states.\
\
Again, this is not guaranteed to work 100% of times, but I think it should succeed most of the times.
# Plans
All the main goals I had for this tool have been finished, but a good addition would be support for other languages, which I could do one day if I really want to.
# Credits and notes
- [GlitchyPSI](https://github.com/GlitchyPSIX) – explaining to me how to fix black textures in save states.
- [HuggingFace](https://huggingface.co/chat/) (an AI) – writing the actual code for fixing black textures because I'm still too dumb to write that myself💀.

Also check out my [M64MM3](https://github.com/projectcomet64/M64MM) add-on that has an option to do what this tool does, but in real time — [Tiny-Huge Tweaks](https://github.com/vazhka-dolya/TinyHugeTweaks)!

This program is not affiliated with or sponsored by Nintendo and does not use any of Nintendo's intellectual property.
