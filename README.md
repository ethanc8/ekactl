# ekactl

[View PDF](kactl.pdf)

## Dependencies

```bash
sudo apt install texlive texlive-science
```

### Using STIX2

```bash
sudo apt install texlive-xetex
tlmgr init-usertree
# Switch 2021 to the correct year according to https://wiki.debian.org/TeXLive
tlmgr option repository ftp://tug.org/historic/systems/texlive/2021/tlnet-final
tlmgr install stix2-otf
```