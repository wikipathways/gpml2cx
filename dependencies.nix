with import <nixpkgs> { config.allowUnfree = true; };
let
  ndex2 = callPackage ./ndex2/default.nix {}; 
in
[
    # Add packages from nix-env -qaP | grep -i needle queries
    ndex2
] ++ (with python37Packages; [
  # python and python packages
  python3
  networkx
  matplotlib
  tkinter
  lxml
])
