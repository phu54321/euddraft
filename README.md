# euddraft

> Note: this repo is not currently maintained. Refer to [armoha's repo](https://github.com/armoha/euddrarft)
> for currently maintained builds.

euddraft is a program for managing [eudplib](https://github.com/phu54321/eudplib) codes into a list of "plugins". Each plugin applies its own functionallity to the map.

Also, `euddraft.exe` serves as a prebuilt binary containing eudplib and all its Python dependencies, so that people without proper Python environment can use eudplib without installing Python.

---

Stock plugins include:

- bgmplayer: Plays looping background music.
- dataDumper: Replace in-game data with user-provided binary via a known pointer.
- eudTurbo: EUD-based turbo trigger, which forces trigger execution on every frame.
- noAirCollision: Prevent air units from repelling each other.
- unlimiter: Remove limits of bullet, sprite counts.
- unpatcher: *(Dangerous)* Undo patching done with `f_dwpatch`.
