# Config

sample home manager config

```nix
{ config, pkgs, ... }:
{
# Home Manager needs a bit of information about you and the paths it should
# manage.
home.username = "herisson";
home.homeDirectory = "/home/herisson";
# This value determines the Home Manager release that your configuration is
# compatible with. This helps avoid breakage when a new Home Manager release
# introduces backwards incompatible changes.
#
# You should not change this value, even if you update Home Manager. If you do
# want to update the value, then make sure to first check the Home Manager
# release notes.
home.stateVersion = "23.05"; # Please read the comment before changing.
nixpkgs.config.allowUnfree = true;
# The home.packages option allows you to install Nix packages into your
# environment.
home.packages = with pkgs; [
cpupower-gui
helix
element-desktop-wayland
headlines
gtkcord4
gotktrix
contrast
lollypop
fragments
shortwave
blanket
btop
htop
zenith
nvtop-amd
unixtools.top
cpu-x
neo-cowsay
thefuck
du-dust
joshuto
celluloid
pipes-rs
pipes
epiphany
#discord
armcord
gnome.dconf-editor
arti
taplo
boringtun
youtube-tui
rx
goxel
clipcat
cmatrix
uutils-coreutils
nushell
clipboard-jh
#(lib.lowPrio uwufetch)
owofetch
pfetch
nano
lfs
lf
gnome.gnome-tweaks
gnome.gnome-terminal
neofetch
hyfetch
adw-gtk3
gradience
firefox-beta-bin
micro
blackbox-terminal
tealdeer
rustpython
downonspot
spotify-tui
dum
cobalt
termusic
skim
dotenv-linter
rustup
mrustc-minicargo
telegram-desktop
#];
# Home Manager is pretty good at managing dotfiles. The primary way to manage
# plain files is through 'home.file'.
#  home.file = {
# # Building this configuration will create a copy of 'dotfiles/screenrc' in
# # the Nix store. Activating the configuration will then make '~/.screenrc' a
# # symlink to the Nix store copy.
# ".screenrc".source = dotfiles/screenrc;
# # You can also set the file content immediately.
# ".gradle/gradle.properties".text = ''
#   org.gradle.console=verbose
#   org.gradle.daemon.idletimeout=3600000
# '';
#  };
# You can also manage environment variables but you will have to manually
# source
#
#  ~/.nix-profile/etc/profile.d/hm-session-vars.sh
#
# or
#
#  /etc/profiles/per-user/herisson/etc/profile.d/hm-session-vars.sh
#
# if you don't want to manage your shell through Home Manager.
#home.packages = [
(pkgs.runCommand "San-Francisco-Pro-Fonts" {
src = pkgs.fetchFromGitHub {
owner = "sahibjotsaggu";
repo = "San-Francisco-Pro-Fonts";
rev = "8bfea09aa6f1139479f80358b2e1e5c6dc991a58";
hash = "sha256-mAXExj8n8gFHq19HfGy4UOJYKVGPYgarGd/04kUIqX4=";
};
} ''
mkdir -p $out/share/fonts/{opentype,truetype}/San-Francisco-Pro-Fonts
cp $src/*.otf $out/share/fonts/opentype/San-Francisco-Pro-Fonts
cp $src/*.ttf $out/share/fonts/truetype/San-Francisco-Pro-Fonts
'')
(pkgs.runCommand "SF-mono-font" {
src = pkgs.fetchFromGitHub {
owner = "supercomputra";
repo = "SF-mono-font";
rev = "1409ae79074d204c284507fef9e479248d5367c1";
hash = "sha256-3wG3M4Qep7MYjktzX9u8d0iDWa17FSXYnObSoTG2I/o=";
};
} ''
mkdir -p $out/share/fonts/{opentype,truetype}/SF-mono-font
cp $src/*.otf $out/share/fonts/opentype/SF-mono-font
#  cp $src/*.ttf $out/share/fonts/truetype/SF-mono-font
'')
];
home.sessionVariables = {
EDITOR = "micro";
};
fonts.fontconfig.enable = true;
# Let Home Manager install and manage itself.
programs.home-manager.enable = true;
gtk = {
enable = true;
gtk3.extraConfig.gtk-decoration-layout = "menu:";
theme.name = "adw-gtk3-dark";
iconTheme = with pkgs; {
name = "Tela-circle-dark";
package = pkgs.tela-circle-icon-theme;
};
};
}
```
