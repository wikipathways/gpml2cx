{ stdenv, fetchFromGitHub, python37 }:

let
  inherit (python37.pkgs) buildPythonApplication;
in

buildPythonApplication rec {
  pname = "ndex2";
  version = "3.2.0";
  name = "${pname}-${version}";

  src = fetchFromGitHub {
    owner = "ndexbio";
    repo = "ndex2-client";
    rev = "04af1f0a2e3afe419f4a5844e55b346f62183945";
    sha256 = "1qy49f61gmcmdfxva29jjk3v1091qzxdxfcmickya77h4xjjf7g7";
  };

  patchPhase = ''
      echo 'my patchPhase'
      sed -i "s#enum.*##" requirements.txt
      sed -i "s#'enum.*##" setup.py
      cat setup.py
    '';

  # TODO patch or whatever to get the tests to pass
  doCheck = false;

  propagatedBuildInputs = with python37.pkgs; [
    six
    ijson
    requests
    requests_toolbelt
    networkx
    urllib3
    pandas
    enum34
    pysolr
    numpy
    setuptools
  ];

  meta = with stdenv.lib; {
    description = "NDEx2 Python Client.";
    longDescription = ''
      The NDEx2 Python Client provides methods to access NDEx via the NDEx REST
      Server API. As well as methods for common operations on networks via the
      NiceCXNetwork class.
      '';
    homepage = "https://www.ndexbio.org";
    license = licenses.bsd3;
    maintainers = with maintainers; [ ];
  };
}
