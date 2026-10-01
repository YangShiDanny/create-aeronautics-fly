package dev.simulated_team.simulated.config.client;

import dev.simulated_team.simulated.config.client.items.SimItemConfigs;
import dev.simulated_team.simulated.config.client.block.SimBlockConfigs;
import com.zurrtum.create.catnip.config.ConfigBase;
import org.jspecify.annotations.NonNull;

public class SimClient extends ConfigBase {
    public final SimItemConfigs itemConfig = this.nested(0, SimItemConfigs::new, SimClient.Comments.itemConfig);
    public final SimBlockConfigs blockConfig = this.nested(0, SimBlockConfigs::new, SimClient.Comments.blockConfig);

    @Override
    @NonNull
    public String getName() {
        return "client";
    }

    private static class Comments {
        static String itemConfig = "Properties of Simulated Items";
        static String blockConfig = "Properties of Simulated Blocks";
    }
}
