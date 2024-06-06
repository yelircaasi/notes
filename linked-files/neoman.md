# Neoman Setup

```sh
* alias nvim-lazy="NVIM_APPNAME=LazyVim nvim"* alias nvim-kick="NVIM_APPNAME=kickstart nvim"* alias nvim-chad="NVIM_APPNAME=NvChad nvim"* alias nvim-astro="NVIM_APPNAME=AstroNvim nvim"
* function nvims() {*   items=("default" "kickstart" "LazyVim" "NvChad" "AstroNvim")*   config=$(printf "%s\n" "${items[@]}" | fzf --prompt=" Neovim Config  " --height=~50% --layout=reverse --border --exit-0)*   # config=$(printf "%s\n" "${items[@]}" | fzf --prompt="<ee><98><ab> Neovim Config <ef><98><bd> " --height=~50% --layout=reverse --border --exit-0)*   if [[ -z $config ]]; then*     echo "Nothing selected"*     return 0*   elif [[ $config == "default" ]]; then*     config=""*   fi*   NVIM_APPNAME=$config nvim $@* }
* bindkey -s ^a "nvims\n"
* ###########* # fish* ###########
* function nvim-chad*     env NVIM_APPNAME=nvim-chad nvim* end
* function nvim-yum*     env NVIM_APPNAME=nvim-yum nvim* end
* function nvims*     set items nvim-yum nvim-chad*     set config (printf "%s\n" $items | fzf --prompt=" Neovim Config  " --height=~50% --layout=reverse --border --exit-0)*     if [ -z $config ]*      echo "Nothing selected"*      return 0*     else if [ $config = "default" ]*      set config ""*     end*     env NVIM_APPNAME=$config nvim $argv* end
* bind \ca 'nvims\n'```
* ###########* # bash v1* ###########
* alias nvim-chad="NVIM_APPNAME=nvim-chad nvim"
* nvims() {*   items=("default" "NvChad")*   config=$(printf "%s\n" "${items[@]}" | fzf --prompt=" Neovim Config  " --height=~50% --layout=reverse --border --exit-0)*   if [[ -z $config ]]; then*     echo "Nothing selected"*     return 0*   elif [[ $config == "default" ]]; then*     config=""*   fi*   NVIM_APPNAME=$config nvim $@* }
* bindkey -s ^a "nvims\n"
* ###########* # bash v2* ###########
* # Neovim config switcher* alias nvim-chad="NVIM_APPNAME=nvim-chad nvim"
* nvims() {*   items=("default" "NvChad")*   config=$(printf "%s\n" "${items[@]}" | fzf --prompt=" Neovim Config  " --height=~50% --layout=reverse --border --exit-0)*   if [[ -z $config ]]; then*     echo "Nothing selected"*     return 0*   elif [[ $config == "default" ]]; then*     config=""*   fi*   NVIM_APPNAME=$config nvim $@* }
* bind -x '"\C-a": nvims'
* ##########################* # for use with lazyman* ##########################
* # $HOME/.config/nvim-Lazyman/.lazymanrc* # This file should be sourced from the shell initialization file* # e.g. $HOME/.bashrc or $HOME/.zshrc* #* # To use Vim* command -v vim > /dev/null && alias vi='vim'* # To use NeoVim* command -v nvim > /dev/null && {*   alias vi='nvim'*   items=()
* [ -d ${HOME}/.config/nvim ] && {*     alias nvim-default="NVIM_APPNAME=nvim nvim"*     items+=("default")*   }*   # Add all previously installed Neovim configurations*   if [ -f ${HOME}/.config/nvim-Lazyman/.nvimdirs ]*   then*     cat ${HOME}/.config/nvim-Lazyman/.nvimdirs | while read nvimdir*     do
* [ -d ${HOME}/.config/${nvimdir} ] && {*      alias ${nvimdir}="NVIM_APPNAME=${nvimdir} nvim"*      entry=$(echo ${nvimdir} | sed -e "s/nvim-//")*      items+=("${entry}")*       }*     done*   else*     # Add any supported config we find
* [ -d ${HOME}/.config/nvim-Lazyman ] && {*       alias nvim-lazy="NVIM_APPNAME=nvim-Lazyman nvim"*       items+=("Lazyman")*     }
* [ -d ${HOME}/.config/nvim-LazyVim ] && {*       alias nvim-lazy="NVIM_APPNAME=nvim-LazyVim nvim"*       items+=("LazyVim")*     }
* [ -d ${HOME}/.config/nvim-Kickstart ] && {*       alias nvim-kick="NVIM_APPNAME=nvim-Kickstart nvim"*       items+=("Kickstart")*     }
* [ -d ${HOME}/.config/nvim-NvChad ] && {*       alias nvim-chad="NVIM_APPNAME=nvim-NvChad nvim"*       items+=("NvChad")*     }
* [ -d ${HOME}/.config/nvim-AstroNvim ] && {*       alias nvim-astro="NVIM_APPNAME=nvim-AstroNvim nvim"*       items+=("AstroNvim")*     }
* [ -d ${HOME}/.config/nvim-Allaman ] && {*       alias nvim-aman="NVIM_APPNAME=nvim-Allaman nvim"*       items+=("Allaman")*     }
* [ -d ${HOME}/.config/nvim-LunarVim ] && {*       alias nvim-lunar="NVIM_APPNAME=nvim-LunarVim nvim"*       items+=("LunarVim")*     }
* [ -d ${HOME}/.config/nvim-MultiVim ] && {*       alias nvim-multi="NVIM_APPNAME=nvim-MultiVim nvim"*       items+=("MultiVim")*     }
* [ -d ${HOME}/.config/nvim-SpaceVim ] && {*       alias nvim-space="NVIM_APPNAME=nvim-SpaceVim nvim"*       items+=("SpaceVim")*     }*   fi
*   function nvims() {*     numitems=${#items[@]}*     if [ ${numitems} -eq 1 ]*     then*       config="${items[@]:0:1}"*     else*       config=$(printf "%s\n" "${items[@]}" | fzf --prompt=" Neovim Config  " --height=60% --layout=reverse --border --exit-0)*     fi*     if [[ -z $config ]]; then*       echo "Nothing selected"*       return 0*     elif [[ $config == "default" ]]; then*       config="nvim"*     else*       if [ -d ${HOME}/.config/nvim-${config} ]*       then*      config="nvim-${config}"*       else
* [ -d ${HOME}/.config/${config} ] || {*        echo "Cannot locate ${config} Neovim configuration directory"*        return 0*      }*       fi*     fi*     NVIM_APPNAME=$config nvim $@*   }*   if [ -n "$($SHELL -c 'echo $ZSH_VERSION')" ]; then*    bindkey -s ^n "nvims\n"*   elif [ -n "$($SHELL -c 'echo $BASH_VERSION')" ]; then*    bind -x '"\C-n": nvims'*   else*    bindkey -s ^n "nvims\n"*   fi* }
* #############* # cool trick* #############
* alias vi="nvim"
* alias nvim-lazy="NVIM_APPNAME=LazyVim nvim"* alias nvim-chad="NVIM_APPNAME=NvChad nvim"* alias nvim-astro="NVIM_APPNAME=AstroNvim nvim"
* function nvims() {*   items=("default" "LazyVim" "NvChad" "AstroNvim")*   config=$(printf "%s\n" "${items[@]}" | fzf --prompt=" Neovim Config  " --height=~50% --layout=reverse --border --exit-0)*   if [[ -z $config ]]; then*     echo "Nothing selected"*     return 0*   elif [[ $config == "default" ]]; then*     config=""*   else*     alias vi="NVIM_APPNAME=${config} nvim"*   fi*   NVIM_APPNAME=$config nvim $@* }
* ##############* # cool script * ##############
* #!/usr/bin/env bash
* # ANSI color codes* RED='\033[0;31m'* YELLOW='\033[1;33m'* GREEN='\033[0;32m'* PURPLE='\033[0;35m'* CYAN='\033[0;36m'* CLEAR='\033[0m'
* DEFAULT_INSTANCE=nvim-default
* show_help() {*   echo -e "Usage: ${YELLOW}nvim-starter ${PURPLE}[COMMAND]${CYAN} [NVIM_OPTIONS...]${CLEAR}"*   echo*   echo "Available commands: (no command start nvim natively)"*   echo -e "  ${PURPLE}sel, select${CLEAR}     Show a selector to choose the Neovim configuration"*   echo -e "  ${PURPLE}def, default${CLEAR}    Start the default instance of Neovim"*   echo -e "  ${PURPLE}help${CLEAR}         Display this help message"* }
* select_config() {*   local items=("default" "nvim" "nvim-learning")*   local config=$(printf "%s\n" "${items[@]}" | fzf --prompt=" Neovim Config: " --height=~50% --layout=reverse --exit-0)
*   if [[ -z $config ]]; then*   echo "${GREEN}Nothing selected${CLEAR}"*   exit 0*   elif [[ $config == "default" ]]; then*   config=$DEFAULT_INSTANCE*   fi
*   NVIM_APPNAME=$config nvim "$@"* }
* default_exec() {*   # Default behavior (no script commds)*   nvim "$@"*   exit 0* }
* ( ) [[ $# -eq 0 ]] && default_exec
* while [[ $# -gt 0 ]]; do*   key="$1"
*   case $key in*   help)*   show_help*   exit 0*   ;;*   sel | select)*   shift # remove the -s or --select*   select_config "$@"*   exit 0*   ;;*   def | default)*   shift # remove the -d or --default*   NVIM_APPNAME=$DEFAULT_INSTANCE nvim "$@"*   exit 0*   ;;*   *)*   default_exec*   ;;*   esac* done
* ##############* # alt version* ##############
* function nvims() {*   local nv_items=("Vanilla" "LazyVim" "NvChad")*   local nv_app=$(printf "%s\n" "${nv_items[@]}" | fzf --prompt=" Neovim Config 󰶻  " --height=~50% --layout=reverse --border --exit-0)
*   if [[ -z $nv_app ]]; then*     echo "Nothing selected"*     return 0*   elif [[ $nv_app == "Vanilla" ]]; then*     nv_app=""*   else*     echo "Set $nvims_config to $nv_app"*   fi
*   echo "$nv_app" > "$nvims_config"*   alias vi="NVIM_APPNAME=${nv_app} nvim"
*   NVIM_APPNAME=$nv_app nvim $@* }
* # nvims* if [[ -x /usr/local/bin/nvim || -x /opt/homebrew/bin/nvim ]]; then*   nvims_config="${XDG_CACHE_HOME:-$HOME/.cache}/nvims"*   nvims_app=$(cat "$nvims_config")*   #echo "Bind Neovim to $nvims_app"*   alias vi="NVIM_APPNAME=${nvims_app} nvim"*   export EDITOR="vi"*   bindkey -s "^v" "nvims\n"* fi

# in terminal input nvims and enter not a valid number: ~50 nothing selected what's wrong?* # any news on this? I do have the same error while just using nvims without any argument. Using WSL2 * bash* # I had the same error.* # Fix was to make height=50% NOT height=~50%* ```

```
