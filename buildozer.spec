[app]

title = VEXA AI
package.name = vexaai
package.domain = org.vexa

source.dir = .
source.include_exts = py,kv,png,jpg

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1