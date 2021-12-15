
function pwafunction (){

const divInstall = document.getElementById('myBtn');
const butInstall = document.getElementById('butInstall');

/* Put code here */
window.addEventListener('beforeinstallprompt', (event) => {
  // Prevent the mini-infobar from appearing on mobile.
  event.preventDefault();
  console.log('👍', 'beforeinstallprompt', event);
  // Stash the event so it can be triggered later.
  window.deferredPrompt = event;
  // Remove the 'hidden' class from the install button container.
  divInstall.classList.toggle('hidden', false);
});

butInstall.addEventListener('click', async () => {
  console.log('👍', 'butInstall-clicked');
  const promptEvent = window.deferredPrompt;
  if (!promptEvent) {
    // The deferred prompt isn't available.
    return;
  }
  // Show the install prompt.
  promptEvent.prompt();
  // Log the result
  const result = await promptEvent.userChoice;
  console.log('👍', 'userChoice', result);
  // Reset the deferred prompt variable, since
  // prompt() can only be called once.
  window.deferredPrompt = null;
  // Hide the install button.
  divInstall.classList.toggle('hidden', true);
});

window.addEventListener('appinstalled', (event) => {
  console.log('👍', 'appinstalled', event);
  // Clear the deferredPrompt so it can be garbage collected
  window.deferredPrompt = null;
});

/* Only register a service worker if it's supported */
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/serviceworker.js');
}

/**
 * Warn the page must be served over HTTPS
 * The `beforeinstallprompt` event won't fire if the page is served over HTTP.
 * Installability requires a service worker with a fetch event handler, and
 * if the page isn't served over HTTPS, the service worker won't load.
 */
if (window.location.protocol === 'http:') {
  const requireHTTPS = document.getElementById('requireHTTPS');
  const link = requireHTTPS.querySelector('a');
  link.href = window.location.href.replace('http://', 'https://');
  requireHTTPS.classList.remove('hidden');
} };

// helps you detect mobile browsers (to show a relevant message as the process of installing your PWA changes from browser to browser)

	var userAgent = window.navigator.userAgent;

if (userAgent.match(/iPad/i) || userAgent.match(/iPhone/i)) {
   console.log("iPad or iPhone");
   document.getElementById("iOS_install").style.display="block";
}
else if (userAgent.match(/Android/i) || userAgent.match(/BlackBerry/i) || userAgent.match(/Opera Mini/i)) {
   console.log("Android Phone");
   document.getElementById("Andriod_install").style.display="block";
   pwafunction();
}
else if (userAgent.match(/SAMSUNG|Samsung|SGH-[I|N|T]|GT-[I|N]|SM-[A|N|P|T|Z]|SHV-E|SCH-[I|J|R|S]|SPH-L/i,)){
	console.log("Samsung Browser");
    document.getElementById("Cannot_Install").style.display="block";
}
else if (userAgent.match(/Windows/i) && userAgent.match(/Chrome/i) ){
	console.log("Windows and Chrome")
    document.getElementById("Andriod_install").style.display="block";
   pwafunction();

}
else if (userAgent.match(/Macintosh/i) && userAgent.match(/Chrome/i) ){
	console.log("Windows and Chrome")
    document.getElementById("Andriod_install").style.display="block";
   pwafunction();
} else{
    document.getElementById("Cannot_Install").style.display="block";
}

if (window.matchMedia('(display-mode: standalone)').matches) {
    document.getElementById("myBtn").style.display ="none";
}