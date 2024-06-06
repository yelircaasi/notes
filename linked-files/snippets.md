# Snippets

## Shell.nix

```nix
let
  pkgs = import <nixpkgs> {};
in
  pkgs.mkShell {
    packages = with pkgs; [
      (python3.withPackages (
    ps: with ps; [
      numpy
      odfpy
      pandas
    ]
      ))
      jupyter
    ];
  }
```

```nix
neovim.package = neovim-nightly.override {
configure = {
packages.myPlugins = with pkgs.vimPlugins; {
start = [
vim-go # already packaged plugin

easygrep # custom package
];
opt = [];
};};

```
* snippet sudo docker run --runtime=nvidia --gpus all -it --rm --dns 8.8.8.8 --dns 8.8.4.4 \ --name nlq \ -v /home/isaac/repos:/root/repos \ -v /home/isaac/data:/root/data \ -v /home/isaac/.ssh:/root/.ssh \ -v /home/isaac/.config/pypoetry:/root/.config/pypoetry \ -v /home/isaac/.cache/torch:/root/.cache/torch \ -v /home/isaac/.cache/huggingface:/root/.cache/huggingface \ nvidia:poetry
snippet1 Dockerfile
snippet2 FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04
snippet3 RUN apt update && apt upgrade && apt install python3 python3-pip
snippet4 RUN python3 -m pip install poetry
snippet7 warning: The option services.xserver.xkbVariant' defined in /nix/store/jybfs22ypnkjqk9hrszazkns8l4kc3yp-source/nixos/hank-configuration.nix' has been renamed to services.xserver.xkb.variant'. trace: warning: The option services.xserver.layout' defined in /nix/store/jybfs22ypnkjqk9hrszazkns8l4kc3yp-source/nixos/hank-configuration.nix' has been renamed to services.xserver.xkb.layout'.
snippet: alias cudaenv="sudo docker run --runtime=nvidia --gpus all -it --rm --dns 8.8.8.8 --dns 8.8.4.4 \ --name 'nlq' \ -v $HOME/dockermounts/nlq-mnt:$HOME/dockermounts/nlq-mnt \ -v /home/isaac/repos:/root/repos \ -v /home/isaac/data:/root/data \ -v /home/isaac/.ssh:/root/.ssh \ -v /home/isaac/.config/pypoetry:/root/.config/pypoetry \ -v /home/isaac/.cache/torch:/root/.cache/torch \ -v /home/isaac/.cache/huggingface:/root/.cache/huggingface \ nvidia:poetry"

## Nix

```nix
* buildPythonPackage {
* pname = "TODO";
* version = "TODO";
* src = fetchPypi {
* inherit pname version;
* sha256 = ""; # TODO

};
```

snippet * deploy = homeManager.makeModule { modules = [ config.nixos ]; };

```nix

{ lib, pkgs, neovimUtils, wrapNeovimUnstable, neovim-nightly-src, ... }:
* let
  binpath = lib.makeBinPath (with pkgs; [
    lua-language-server
    stylua

    nodePackages.prettier
    nodePackages.pyright

    # I can't install this with the rest of the python packages b/c this needs to be in path
    python3Packages.jupytext
    lua
  ]);
  neovimConfig = pkgs.neovimUtils.makeNeovimConfig {
    extraLuaPackages = p: [ p.magick ];
    extraPython3Packages = p: with p; [
      pynvim
      jupyter-client
      cairosvg
      ipython
      nbformat
    ];
    extraPackages = p: with p; [
      imageMagick
    ];
    withNodeJs = true;
    withRuby = true;
    withPython3 = true;
    # [NixOS/nixpkgs/issues/211998](https://github.com/NixOS/nixpkgs/issues/211998)
    customRC = "luafile ~/.config/nvim/init.lua";
  };
* in

{
  nixpkgs.overlays = [
    (_: super: {
      neovim-custom = pkgs.wrapNeovimUnstable
        # (neovim-nightly.overrideAttrs (oldAttrs: {
        (super.neovim-unwrapped.overrideAttrs (oldAttrs: {
          buildInputs = oldAttrs.buildInputs ++ [ super.tree-sitter ];
          src = neovim-nightly-src;
        }))
        (neovimConfig // {
          wrapperArgs = lib.escapeShellArgs neovimConfig.wrapperArgs
            + " --prefix PATH : ${binpath}";
        });
    })
  ];

  environment.systemPackages = with pkgs; [
    neovim-custom
  ];

}

```

FIXME### Haskell CLI in Flake

```sh
my-haskell-flake/
├── src/
│   └── Main.hs        # Haskell source file containing your CLI program
├── flake.nix          # Nix flake definition
└── default.nix        # Optional, used if you prefer to use default.nix for overrides
```

```hs
-- src/Main.hs
module Main where
* import Options.Applicative
* data Options = Options
  { name :: String
  } deriving (Show)
* parseOptions :: Parser Options
parseOptions = Options
  <$> strOption
    ( long "name"
    <> short 'n'
    <> metavar "NAME"
    <> help "Your name" )
* main :: IO ()
main = do
  options <- execParser opts
  putStrLn $ "Hello, " ++ name options ++ "!"
  where
    opts = info (parseOptions <**> helper)
      ( fullDesc
     <> progDesc "Print a greeting for NAME"
     <> header "hello - a simple greeting program" )
```

```nix

FIXME# flake.nix

{
  description = "My Haskell Flake with CLI functionality";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
  };

  outputs = { self, nixpkgs }: {
    # Define an executable output that builds and runs the Haskell CLI program
    executable = {
      # Specify the path to your Haskell source file
      command = "src/Main.hs";

      # Optionally specify additional dependencies
      # dependencies = [ pkgs.haskellPackages.somePackage ];

      # Optionally specify environment variables or other settings
    };
  };
}
```

```nix

FIXME# tree.nix

{ lib, nixpkgs ? import <nixpkgs> {} }:
* let

FIXME# Function to print a tree structure

printTree = prefix: node: tree:
* if lib.isAttrs node
* then
* let
* attrs = lib.attrValues node;
* attrNames = lib.attrNames node;
* lines = lib.mapAttrsToList (name: value: "${name}: ${value}") node;
* subtree = lib.mapAttrsToList (name: value: printTree (prefix + "  ") value tree) node;
* in
* if lib.length attrs > 0
* then "${prefix}${lib.concatStringsSep "\\n" (lib.mapAttrsToList (name: value: "${name}: ${value}") node)}"
* else

"${prefix}${lib.concatStringsSep "\\n" (lib.mapAttrsToList (name: value: "${value}") node)}"

+ (lib.concatStringsSep "\\n" subtree)
* else "${prefix}${node}";

FIXME# Function to build the import tree

* buildImportTree = derivation:
* let
* buildTree = drv:
* let
* inputs = lib.foldl' (acc: input: acc + [input])
* [] drv.buildInputs;
* in

{ ${lib.foldl' (acc: input: acc + [input]) "" inputs} } // (lib.foldl' (acc: input: acc + buildTree input) {} inputs);
* importTree = buildTree derivation;
* in
* printTree "" importTree importTree;
* in

{ buildImportTree, printTree }
* This script defines two functions: printTree for printing the tree structure and buildImportTree for building the import tree. The example assumes you have the nixpkgs attribute set available.To use this script, you can import it into another Nix expression and call the buildImportTree function, passing the derivation for the desired output. For example:nixCopy code
```

```nix

FIXME# example.nix

{ lib, nixpkgs ? import <nixpkgs> {}, tree ? import ./tree.nix { nixpkgs = nixpkgs; } }:
* let
* myOutput = nixpkgs.myPackage.outputs.defaultPackage.x86_64-linux;
* importTree = tree.buildImportTree myOutput;
* in
* tree.printTree "" importTree importTree
```

```nix
buildPythonPackage {
  pname = "TODO";
  version = "TODO";
  src = fetchPypi {
  inherit pname version;
  sha256 = ""; # TODO
};
```

 You How could I print out a tree representation of the imports of a given output?ChatGPTChatGPT To print out a tree representation of the imports of a given output in a Nix flake, you can leverage the nixpkgs attribute set and the buildInputs attribute of the derivation for the specified output. You can create a recursive function to traverse the import tree and print it in a tree-like structure.Here's an example script in Nix that demonstrates how you can achieve this

```nix

FIXME# tree.nix

{ lib, nixpkgs ? import <nixpkgs> {} }:
let
  # Function to print a tree structure
  printTree = prefix: node: tree:
    if lib.isAttrs node
  then let
    attrs = lib.attrValues node;
    attrNames = lib.attrNames node;
    lines = lib.mapAttrsToList (name: value: "${name}: ${value}") node;
    subtree = lib.mapAttrsToList (name: value: printTree (prefix + "  ") value tree) node;
  in
    if lib.length attrs > 0
    then "${prefix}${lib.concatStringsSep "\\n" (lib.mapAttrsToList (name: value: "${name}: ${value}") node)}"
    else "${prefix}${lib.concatStringsSep "\\n" (lib.mapAttrsToList (name: value: "${value}") node)}" + (lib.concatStringsSep "\\n" subtree)
* else "${prefix}${node}";

FIXME# Function to build the import tree

* buildImportTree = derivation:
* let
* buildTree = drv:
* let
* inputs = lib.foldl' (acc: input: acc + [input])
* [] drv.buildInputs;
* in

{ ${lib.foldl' (acc: input: acc + [input]) "" inputs} } // (lib.foldl' (acc: input: acc + buildTree input) {} inputs);
* importTree = buildTree derivation;
* in
* printTree "" importTree importTree;
* in

{ buildImportTree, printTree }
* This script defines two functions: printTree for printing the tree structure and buildImportTree for building the import tree. The example assumes you have the nixpkgs attribute set available.To use this script, you can import it into another Nix expression and call the buildImportTree function, passing the derivation for the desired output. For example:nixCopy code

FIXME# example.nix

{ lib, nixpkgs ? import <nixpkgs> {}, tree ? import ./tree.nix { nixpkgs = nixpkgs; } }:
* let
* myOutput = nixpkgs.myPackage.outputs.defaultPackage.x86_64-linux;
* importTree = tree.buildImportTree myOutput;
* in
* tree.printTree "" importTree importTree
```

* Replace myPackage with the actual package name or output you want to inspect. Running the example.nix script should print the import tree structure for the specified output.

* Flake CLI QuestionHow can I add a CLI functionality to a Nix flake?ChatGPTChatGPT To add command-line interface (CLI) functionality to a Nix flake, you can use the programs attribute in the flake's outputs section. Here's a step-by-step guide:
* Create a directory structure: In your flake's directory, create a directory for your CLI program. For example:plaintextCopy code
* my-flake/

```txt
├── flake.nix

└── src/

└── my-cli/

└── Main.hs
* 1.
* Write your CLI program: Write your CLI program in the Main.hs file. For example:haskellCopy code
* - src/my-cli/Main.hs
* module Main where
* import System.Environment
* main :: IO ()
* main = do
* args <- getArgs
* putStrLn $ "Hello, CLI! Args: " ++ show args
* 1.
* Update your flake.nix file: Update your flake.nix file to include the programs attribute. Here's an example:nixCopy code

{
* description = "My Flake with CLI";
* inputs = {
* nixpkgs.url = "github:nixos/nixpkgs/nixos-21.11";

};
* outputs = { self, nixpkgs }: {
* defaultPackage.x86_64-linux = self.packages.haskellPackages.callPackage ./src/my-cli {};
* programs.hello-cli = {
* enable = true;
* package = self.defaultPackage.x86_64-linux;

};

};

}
```

* 1. In this example, hello-cli is the name of your CLI program. The package attribute points to the Haskell package generated from your source code.
* Build and run your CLI program: Run the following commands to build and run your CLI program:bashCopy code
* nix build
* ./result/bin/hello-cli
* 1. Replace hello-cli with the name you specified in your programs attribute.
* Now, your Nix flake includes a CLI program that can be easily built and run. You can customize the programs attribute further based on your specific requirements. [...](https://lh3.googleusercontent.com/a/AEdFTp7iti-r88FvOL2bvykuZfqt0KtgKeReZeLGIIrZyA%3Ds96-c)
* [...](https://lh3.googleusercontent.com/a/AEdFTp7iti-r88FvOL2bvykuZfqt0KtgKeReZeLGIIrZyA%3Ds96-c) You What are the possible values for the atributes of the output of a flake?ChatGPTChatGPT In a Nix flake, the outputs attribute is used to specify the outputs that will be produced by the flake. Each output can have its own set of attributes. Here are some common attributes that can be used in the outputs section of a flake:
* defaultPackage: This attribute specifies the default output for the flake. It usually points to the main result produced by the flake. For example:nixCopy code


```txt
* outputs = { self, nixpkgs }: {
* defaultPackage.x86_64-linux = self.packages.x86_64-linux.myPackage;

};
* 1.
* packages: This attribute is used to define one or more packages produced by the flake. Each package can have its own set of attributes like packagePrefix, meta, etc.nixCopy code
* outputs = { self, nixpkgs }: {
* packages.x86_64-linux.myPackage = self.packages.haskellPackages.myHaskellPackage;

};
* 1.
* programs: This attribute is used to define executable programs produced by the flake. It allows you to specify which packages to use and whether the program should be enabled or not.nixCopy code
* outputs = { self, nixpkgs }: {
* programs.myProgram = {
* enable = true;
* package = self.packages.x86_64-linux.myPackage;

};

};
* 1.
* documentation: This attribute is used to specify documentation generated by the flake. It can include attributes like html, man, etc.nixCopy code
* outputs = { self, nixpkgs }: {
* documentation.html = self.defaultPackage.x86_64-linux + "/share/doc/myPackage/html";

};
* 1.
* dev: This attribute is used to specify development files produced by the flake.nixCopy code
* outputs = { self, nixpkgs }: {
* dev = self.defaultPackage.x86_64-linux + "/lib/myPackage-dev";

};
* 1.
* These are just examples, and the actual attributes you use will depend on the nature of your flake and the kind of outputs you want to produce. The key is to define the outputs you need and customize their attributes accordingly. Always refer to the Nixpkgs manual or Nix documentation for the most up-to-date and detailed information on available attributes. [...](https://lh3.googleusercontent.com/a/AEdFTp7iti-r88FvOL2bvykuZfqt0KtgKeReZeLGIIrZyA%3Ds96-c)
* [...](https://lh3.googleusercontent.com/a/AEdFTp7iti-r88FvOL2bvykuZfqt0KtgKeReZeLGIIrZyA%3Ds96-c) You How could I print out a tree representation of the imports of a given output?ChatGPTChatGPT To print out a tree representation of the imports of a given output in a Nix flake, you can leverage the nixpkgs attribute set and the buildInputs attribute of the derivation for the specified output. You can create a recursive function to traverse the import tree and print it in a tree-like structure.Here's an example script in Nix that demonstrates how you can achieve this:nixCopy code
* Replace myPackage with the actual package name or output you want to inspect. Running the example.nix script should print the import tree structure for the specified output.
```

* code * [t.me](https://t.me/nixos_en/114808?single)
