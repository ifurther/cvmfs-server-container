Name:       cvmfs-REPO_NAME_REPLACE_ME-pub-key
Version:    1
Release:    1
Summary:    Public key distribution package for REPO_NAME_REPLACE_ME CVMFS repository.
License:    FIXME

%description
This RPM handles the public key distribution for the REPO_NAME_REPLACE_ME CVMFS repository.

%prep
# we have no source, so nothing here

%build
cat %{buildroot}/etc/cvmfs/keys/REPO_NAME_REPLACE_ME.pub > REPO_NAME_REPLACE_ME.pub

%install
mkdir -p %{buildroot}/etc/cvmfs/keys
install -m 600 REPO_NAME_REPLACE_ME.pub %{buildroot}/etc/cvmfs/keys/REPO_NAME_REPLACE_ME.pub

%files
REPO_NAME_REPLACE_ME.pub

%changelog
# let's skip this for now