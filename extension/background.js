
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    console.log("Message received in content script:", message);
    sendResponse({ reply: "Hello from content script" });
});
console.log("background script loaded");