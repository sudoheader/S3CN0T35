# Set Up on QEMU/KVM (virt-manager on linux)
### ⚠️DISCLAIMER⚠️: You don't need to follow this if you can get the Blue VM to work on either VirtualBox or VMware.

While you can import the `Blue.ovf` from the Capstone Google Drive folder into VirtualBox or VMware, there is another way to do this, albeit a bit lengthier, to get it working in `virt-manager`. This method is mainly intended to get the vm working on a Linux platform (like Arch Linux with an XFCE or dwm windows manager) but if you are capable of figuring out problems than follow this guide.

First download the `Blue.7z` file from Google Drive. Extract however you want (use either the `Archive Manager` or `7z` and then make sure to install a few tools before continuing. In Arch Linux and its derivatives, install these `pacman` packages.
#todo

#### Extracting using 7z
`7z x Blue.7z -oBlue` will extract all contents of `Blue.7z` into the `Blue` folder. Usage of `-o{Directory}` should be before the name of the output folder with no spaces.

## What you need
If you are already on Linux like me, you might want to either do this Capstone in VirtualBox or `virt-manager`. I have encountered problems in trying to import the `.ovf` file into VMware Workstation (at least this seems to be relevant only on Linux) so I'll be doing these capstones on that since I already have a Kali VM that I use with `virt-manager`. Anyway, depending on you setup, you'll need the following:

### Arch Linux
#TODO finish this part
1. `sudo pacman -Syu`
2. `sudo pacman -S qemu-img `

Make sure to download this iso file so that we can get network access in the vm: https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/virtio-win-0.1.189-1/

Download the `virtio-win-0.1.189.iso` one since it works for me.

## Converting our `vmdk` to `qcow2`
Change directory to where we extracted the `Blue.7z`. In my case, it was the `Blue` folder.

Now you'll need to convert the `Blue-disk001.vmdk` into `qcow2` so that we can import it into `virt-manager`

```bash
qemu-img convert -O qcow2 Blue-disk001.vmdk Blue.qcow2
```

It'll take a few minutes depending on how large the `vmdk` or how many `vmdk` files we have.

1. Now all you need to do is open up `virt-manager` and depending how you have set it up (there are a few guides online), you'll need to import a new OS, so click on the "plus" button that says "Create a new virtual machine". 
2. Next select from the menu "Import existing disk image" and click on "Forward". 
3. On the second screen click on "Browse..." and then click on "Browse Local", which will bring you to your File Browser. Go to wherever you have converted the `Blue.qcow2` disk image and click on "Open". You will also need to click on the search box and search for "vista" but in this case make sure to click on the checkbox where it says "Include end of life operating systems". You should see "Microsoft Windows Vista (winvista)" so select that one. Click on "Forward".
4. You can leave the "Choose Memory and CPU settings" alone for the time being depending on your setup. You still have the option to change them in the future. Click on "Forward".
5. Rename the VM to "Blue" if you want and also click on the check box for "Customize configuration before install" since we will need one additional step before starting the vm. Also click on the dropdown menu where it says "Network selection" and make sure it is by default set to "NAT", otherwise you will not have network on the VM. Click "Finish".
6. The last thing will be to "Add Hardware" so click on the button and click on "Select or create custom storage" and click on the "Manage..." button. Click on "Browse Local" and find the `virtio-win-0.1.189.iso` that we downloaded. Click on "Open" and for "Device Type" select "CDROM device" and "Bus type" select "SATA". Click "Finish" when you're done.
7. You can now click on "Begin Installation" and it should boot up the VM.

Go to the `Blue Walkthough` to follow the rest of the guide.