with import <nixpkgs> { config.allowUnfree = true; };

{
  ndex2 = callPackage ./ndex2/default.nix {}; 
}
