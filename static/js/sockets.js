// WebSocket client library

angular.module('Sockets_Library', ['ngWebSocket'])
.controller('Weight_Socket', ['$scope', '$websocket', function($scope, $websocket) {
    $websocket('ws://localhost:5001').onMessage(function(message) {
        $scope.weight = JSON.parse(message.data).data;
    });
}]);