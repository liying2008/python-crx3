chrome.runtime.onInstalled.addListener(({ reason }) => {
  console.log(reason)
  sayWelcome();

  if (chrome.alarms.onAlarm.hasListener(sayWelcome)) {
    chrome.alarms.onAlarm.removeListener(sayWelcome);
  }
  chrome.alarms.onAlarm.addListener(sayWelcome);

  chrome.alarms.create('demo-default-alarm', {
    delayInMinutes: 1,
    periodInMinutes: 1
  });
});

function sayWelcome() {
  console.log('Welcome!')
}
