function openSidebar(link) {
  var sidebarItem = link.parentElement;

  // Close all sidebar items first
  var sidebarItems = document.querySelectorAll(".sidebar a");
  sidebarItems.forEach(function (item) {
    item.parentElement.style.width = "85px";
  });

  // Open the hovered sidebar item
  sidebarItem.style.width = "250px";
}

function closeSidebar(link) {
  var sidebarItem = link.parentElement;

  // Close the hovered sidebar item
  sidebarItem.style.width = "85px";
}