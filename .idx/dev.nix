{ pkgs ? import <nixpkgs> {} }:

let
  pythonEnv = pkgs.python311.withPackages (ps: with ps; [
    pip
    flask
    tensorflow
    pillow
    numpy
    matplotlib
  ]);
in

pkgs.mkShell {
  buildInputs = [ pythonEnv ];
}


